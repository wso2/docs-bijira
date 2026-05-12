import re

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
