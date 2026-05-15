import re
import os
import hashlib


def _file_hash(path: str) -> str:
    """Return the first 8 hex characters of the MD5 hash of a file's content."""
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def on_post_build(config, **kwargs):
    """Append content-hash query strings to @import URLs inside the built theme.css
    so that CDN / browser caches are busted whenever a partial file changes."""
    site_dir = config["site_dir"]
    theme_css_path = os.path.join(site_dir, "assets", "css", "theme.css")

    if not os.path.exists(theme_css_path):
        return

    partials_dir = os.path.join(site_dir, "assets", "css", "partials")

    with open(theme_css_path, "r", encoding="utf-8") as f:
        content = f.read()

    def _add_hash(match):
        url = match.group(1)
        # Strip any existing query string before recomputing
        base_url = url.split("?")[0]
        partial_path = os.path.join(partials_dir, os.path.basename(base_url))
        if os.path.exists(partial_path):
            version = _file_hash(partial_path)
            return f"@import url('{base_url}?v={version}')"
        return match.group(0)

    new_content = re.sub(r"@import url\('([^']+)'\)", _add_hash, content)

    with open(theme_css_path, "w", encoding="utf-8") as f:
        f.write(new_content)


def on_post_page(output, page, config, **kwargs):
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
