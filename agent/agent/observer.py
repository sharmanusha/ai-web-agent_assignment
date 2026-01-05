async def observe_page(page):
    title = await page.title()
    body_text = await page.inner_text("body")

    buttons = await page.query_selector_all("button")
    links = await page.query_selector_all("a")

    return {
        "title": title,
        "button_count": len(buttons),
        "link_count": len(links),
        "text_preview": body_text[:400]
    }
