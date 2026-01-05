import asyncio
from dotenv import load_dotenv
load_dotenv()

from playwright.async_api import async_playwright
from agent.observer import observe_page
from agent.decision_maker import decide_action
from agent.actor import act
from agent.logger import log_step


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto(
            "https://books.toscrape.com",
            wait_until="domcontentloaded",
            timeout=60000
        )

        await page.wait_for_selector("article.product_pod")

        # --- AGENT STEP ---
        observation = await observe_page(page)
        decision = decide_action(observation)

        log_step({
            "step": 0,
            "observation": observation,
            "decision": decision
        })

        # 🔥 GUARANTEED VISIBLE ACTION
        await act(page, decision)

        # 👀 Keep browser open so you can SEE it
        await page.wait_for_timeout(8000)

        await browser.close()


if __name__ == "__main__":
    asyncio.run(run())
