async def act(page, decision):
    # Click first visible book and wait for navigation
    book = await page.query_selector("article.product_pod h3 a")

    if not book:
        return False

    await book.click()
    await page.wait_for_load_state("domcontentloaded")
    return True
