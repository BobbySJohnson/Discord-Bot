import asyncio
from pyppeteer import launch


async def start_chrome():
    global browser
    browser = await launch(headless=True, ignoreHTTPSErrors=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
    page = await browser.newPage()
    await page.goto("https://ifconfig.me")


async def take_screenshot(url, file_name, width, height):

    page = await browser.newPage()
    await page.setViewport({
      "width": width,
      "height": height
    })
    await page.goto(url, {'waitUntil' : 'domcontentloaded'})
    #await asyncio.sleep(1)
    await page.screenshot({'path': file_name})
    await page.close()

async def take_screenshot_runner(url, file_name, width, height):
  task1 = asyncio.create_task(take_screenshot(url, file_name, width, height))
  await task1



#### SCREENER ####
async def do_browsing(order, to_show, columns):

    page = await browser.newPage()
    await page.setViewport({
      "width": 1024,
      "height": 768
    })
    await page.goto('https://s.tradingview.com/embed-widget/screener/#%7B%0A%20%20%22width%22%3A%201100%2C%0A%20%20%22height%22%3A%20512%2C%0A%20%20%22defaultColumn%22%3A%20%22overview%22%2C%0A%20%20%22defaultScreen%22%3A%20%22general%22%2C%0A%20%20%22market%22%3A%20%22forex%22%2C%0A%20%20%22showToolbar%22%3A%20true%2C%0A%20%20%22colorTheme%22%3A%20%22light%22%2C%0A%20%20%22locale%22%3A%20%22en%22%0A%7D')
    await asyncio.sleep(1)
    
    drop_box = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]")
    await drop_box[0].click()

    count = 1
    while count < 9:
      unusable = await page.xpath(f"/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[{count}]/label/label/span[1]")
      await unusable[0].click()
      count += 1

    for column in columns:
      if column == "1m":
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[66]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == "15m":
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[62]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == '5m':
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[70]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == "1h":
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[64]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == "4h":
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[68]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == "1mn":
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[65]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == "15mn":
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[61]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == '5mn':
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[69]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == "1hn":
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[63]/label/label/span[1]")
        await click_checkbox[0].click()
      elif column == "4hn":
        click_checkbox = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[67]/label/label/span[1]")
        await click_checkbox[0].click()




##########################################

    dropdown_remove = await page.xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]")
    await dropdown_remove[0].click()
    await asyncio.sleep(1)
########################################
    too_show = int(to_show) + 1
    xp = f'/html/body/div[1]/div[2]/div/div[3]/table/thead/tr/th[{too_show}]/div/div/div/div'
    ord = await page.xpath(xp)

    if order == 'des':
      await ord[0].click()
    elif order == "aes":
      await ord[0].click()
      await ord[0].click()


    await asyncio.sleep(1)
    await page.screenshot({'path': 's.png'})
    await browser.close()

async def screener_runner(order, to_show, columns):
  task1 = asyncio.create_task(do_browsing(order, to_show, columns))
  await task1