import asyncio
from pyppeteer import launch

async def take_screenshot(url, file_name, width, height):

    browser = await launch(headless=True, ignoreHTTPSErrors=True, args=['--no-sandbox', '--disable-setuid-sandbox'])

    page = await browser.newPage()
    await page.setViewport({
      "width": width,
      "height": height
    })
    await page.goto(url)
    await asyncio.sleep(2)
    await page.screenshot({'path': file_name})
    await page.close()

async def take_screenshot_runner(url, file_name, width, height):
  task1 = asyncio.create_task(take_screenshot(url, file_name, width, height))
  await task1
