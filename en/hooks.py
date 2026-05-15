import re
import os
import hashlib

_HOOKS_DIR = os.path.dirname(os.path.abspath(__file__))

# Populated in on_pre_build; used by on_post_page and on_post_build.
_partial_hashes: dict[str, str] = {}
_theme_css_version: str = ""


def _file_hash(path: str) -> str:
    """Return the first 8 hex characters of the MD5 hash of a file's content."""
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def on_pre_build(config, **kwargs):
    """Pre-compute content hashes from source CSS files.

    The combined hash of theme.css + every partial is stored as the version
    string added to the <link> tag in HTML, so any change to any partial also
    busts the theme.css browser/CDN cache.
    """
    global _theme_css_version
    _partial_hashes.clear()

    css_src_dir = os.path.join(_HOOKS_DIR, "theme", "material", "assets", "css")
    partials_src_dir = os.path.join(css_src_dir, "partials")

    # Collect raw bytes of theme.css + all partials for a combined hash
    combined = bytearray()

    theme_css_src = os.path.join(css_src_dir, "theme.css")
    if os.path.exists(theme_css_src):
        with open(theme_css_src, "rb") as f:
            combined += f.read()

    if os.path.exists(partials_src_dir):
        for fname in sorted(os.listdir(partials_src_dir)):
            if fname.endswith(".css"):
                path = os.path.join(partials_src_dir, fname)
                data = open(path, "rb").read()
                combined += data
                _partial_hashes[fname] = hashlib.md5(data).hexdigest()[:8]

    _theme_css_version = hashlib.md5(combined).hexdigest()[:8]


def on_post_build(config, **kwargs):
    """Append content-hash query strings to @import URLs inside the built theme.css
    so that CDN / browser caches are busted whenever a partial file changes."""
    site_dir = config["site_dir"]
    theme_css_path = os.path.join(site_dir, "assets", "css", "theme.css")

    if not os.path.exists(theme_css_path):
        return

    with open(theme_css_path, "r", encoding="utf-8") as f:
        content = f.read()

    def _add_hash(match):
        url = match.group(1)
        base_url = url.split("?")[0]
        fname = os.path.basename(base_url)
        version = _partial_hashes.get(fname)
        if version:
            return f"@import url('{base_url}?v={version}')"
        return match.group(0)

    new_content = re.sub(r"@import url\('([^']+)'\)", _add_hash, content)

    with open(theme_css_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def on_post_page(output, page, config, **kwargs):
    # Add cache-busting version to the theme.css <link> tag so CDN/browser
    # cache is invalidated whenever theme.css or any of its partials change.
    if _theme_css_version:
        output = re.sub(
            r'(<link[^>]+href="[^"]*assets/css/theme\.css)(")',
            rf'\1?v={_theme_css_version}\2',
            output,
        )

    if page.is_homepage:
        return output

    first = next(iter(page.toc), None)
    if first:
        title = re.sub(r"<[^>]+>", "", first.title).strip()
    elif page.meta and page.meta.get("title"):
        title = page.meta["title"]
    elif page.title:
        title = re.sub(r"<[^>]+>", "", page.title).strip()
    else:
        return output

    suffix = config.get("extra", {}).get("page_title_suffix", "")
    full_title = f"{title} | {suffix}" if suffix else title

    return re.sub(r"<title>.*?</title>", f"<title>{full_title}</title>", output, count=1)
