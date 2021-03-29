import asyncio
from pyppeteer import launch
from discord_webhook import DiscordWebhook

webhook_url = "https://discord.com/api/webhooks/825061165784629298/gVNhqcV0NOIorhs-jYnBGbDbCKjaHT-2d569kXLNERX4rBcYM1JYGrwJ8wyttW88ov6q"


async def start_chrome():
    global browser
    browser = await launch(headless=True,
                           ignoreHTTPSErrors=True,
                           args=['--no-sandbox', '--disable-setuid-sandbox'])


async def process_chart(pair, time_frame):
    BB_UP = 4
    BB_DOWN = 2
    WMA_5H = 2
    WMA_5L = 2
    WMA_10H = 4
    WMA_10L = 4
    page = await browser.newPage()
    await page.setViewport({"width": 800, "height": 600})
    try:
        url = f'https://s.tradingview.com/widgetembed/?frameElementId=tradingview_33e44&symbol=fx%3A{pair}&interval={time_frame}&hidetoptoolbar=1&symboledit=1&saveimage=0&toolbarbg=f1f3f6&studies=BB%40tv-basicstudies%1FMAWeighted%40tv-basicstudies%1FMAWeighted%40tv-basicstudies%1FMAWeighted%40tv-basicstudies%1FMAWeighted%40tv-basicstudies%1F&theme=light&style=1&timezone=Etc%2FUTC&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=en'
        await page.goto(url, {'waitUntil': 'load'})

        #### FIRST ####
        await page.click(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane > div > div.noWrap-2KhwsEwE.legend-2KhwsEwE.newCollapser-2KhwsEwE > div.sourcesWrapper-2KhwsEwE > div.sources-2KhwsEwE > div:nth-child(3) > div.noWrapWrapper-2KhwsEwE > div.titleWrapper-2KhwsEwE > div.title-2KhwsEwE.title1st-2KhwsEwE.apply-overflow-tooltip.withDot-2KhwsEwE"
        )
        await asyncio.sleep(0.5)
        await page.click(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane > div > div.noWrap-2KhwsEwE.legend-2KhwsEwE.newCollapser-2KhwsEwE > div.sourcesWrapper-2KhwsEwE > div.sources-2KhwsEwE > div.item-2KhwsEwE.study-2KhwsEwE.invisibleHover-2KhwsEwE.withTail-2KhwsEwE.selected-2KhwsEwE > div.noWrapWrapper-2KhwsEwE > div.buttonsWrapper-2KhwsEwE > div > div:nth-child(2) > div"
        )
        await asyncio.sleep(0.5)
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(2) > div > div"
        )
        await page.keyboard.press("Backspace")
        await page.type(
            '#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(2) > div > div > div > div > div.innerInputContainer-21h1g6jU > input',
            "5")
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(4) > div > div > span > span"
        )
        await page.click(
            "#overlap-manager-root > div > div > div:nth-child(2) > div > span > div.dropdownMenu-1zfqRRWX.menuWrap-g78rwseC > div > div > div:nth-child(2) > div > div"
        )
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.footer-KW8170fm > div.buttons-KW8170fm > span > button > span"
        )
        #await asyncio.sleep(1)

        #### SECOND ####
        await page.click(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane > div > div.noWrap-2KhwsEwE.legend-2KhwsEwE.newCollapser-2KhwsEwE > div.sourcesWrapper-2KhwsEwE > div.sources-2KhwsEwE > div:nth-child(4) > div.noWrapWrapper-2KhwsEwE > div.titleWrapper-2KhwsEwE > div.title-2KhwsEwE.title1st-2KhwsEwE.apply-overflow-tooltip.withDot-2KhwsEwE"
        )
        await asyncio.sleep(0.5)
        await page.click(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane > div > div.noWrap-2KhwsEwE.legend-2KhwsEwE.newCollapser-2KhwsEwE > div.sourcesWrapper-2KhwsEwE > div.sources-2KhwsEwE > div.item-2KhwsEwE.study-2KhwsEwE.invisibleHover-2KhwsEwE.withTail-2KhwsEwE.selected-2KhwsEwE > div.noWrapWrapper-2KhwsEwE > div.buttonsWrapper-2KhwsEwE > div > div:nth-child(2) > div"
        )
        await asyncio.sleep(0.5)
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(2) > div > div"
        )
        await page.keyboard.press("Backspace")
        await page.type(
            '#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(2) > div > div > div > div > div.innerInputContainer-21h1g6jU > input',
            "5")
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(4) > div > div > span > span"
        )
        await page.click(
            "#overlap-manager-root > div > div > div:nth-child(2) > div > span > div.dropdownMenu-1zfqRRWX.menuWrap-g78rwseC > div > div > div:nth-child(3) > div > div"
        )
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.footer-KW8170fm > div.buttons-KW8170fm > span > button > span"
        )

        #### THIRD ####
        await page.click(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane > div > div.noWrap-2KhwsEwE.legend-2KhwsEwE.newCollapser-2KhwsEwE > div.sourcesWrapper-2KhwsEwE > div.sources-2KhwsEwE > div:nth-child(5) > div.noWrapWrapper-2KhwsEwE > div.titleWrapper-2KhwsEwE > div.title-2KhwsEwE.title1st-2KhwsEwE.apply-overflow-tooltip.withDot-2KhwsEwE"
        )
        await asyncio.sleep(0.5)
        await page.click(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane > div > div.noWrap-2KhwsEwE.legend-2KhwsEwE.newCollapser-2KhwsEwE > div.sourcesWrapper-2KhwsEwE > div.sources-2KhwsEwE > div.item-2KhwsEwE.study-2KhwsEwE.invisibleHover-2KhwsEwE.withTail-2KhwsEwE.selected-2KhwsEwE > div.noWrapWrapper-2KhwsEwE > div.buttonsWrapper-2KhwsEwE > div > div:nth-child(2) > div"
        )
        await asyncio.sleep(0.5)
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(2) > div > div"
        )
        await page.keyboard.press("Backspace")
        await page.type(
            '#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(2) > div > div > div > div > div.innerInputContainer-21h1g6jU > input',
            "10")
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(4) > div > div > span > span"
        )
        await page.click(
            "#overlap-manager-root > div > div > div:nth-child(2) > div > span > div.dropdownMenu-1zfqRRWX.menuWrap-g78rwseC > div > div > div:nth-child(2) > div > div"
        )
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.footer-KW8170fm > div.buttons-KW8170fm > span > button > span"
        )

        #### FOuRTH ####
        await page.click(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane > div > div.noWrap-2KhwsEwE.legend-2KhwsEwE.newCollapser-2KhwsEwE > div.sourcesWrapper-2KhwsEwE > div.sources-2KhwsEwE > div:nth-child(6) > div.noWrapWrapper-2KhwsEwE > div.titleWrapper-2KhwsEwE > div.title-2KhwsEwE.title1st-2KhwsEwE.apply-overflow-tooltip.withDot-2KhwsEwE"
        )
        await asyncio.sleep(0.5)
        await page.click(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(1) > td.chart-markup-table.pane > div > div.noWrap-2KhwsEwE.legend-2KhwsEwE.newCollapser-2KhwsEwE > div.sourcesWrapper-2KhwsEwE > div.sources-2KhwsEwE > div.item-2KhwsEwE.study-2KhwsEwE.invisibleHover-2KhwsEwE.withTail-2KhwsEwE.selected-2KhwsEwE > div.noWrapWrapper-2KhwsEwE > div.buttonsWrapper-2KhwsEwE > div > div:nth-child(2) > div"
        )
        await asyncio.sleep(0.5)
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(2) > div > div"
        )
        await page.keyboard.press("Backspace")
        await page.type(
            '#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(2) > div > div > div > div > div.innerInputContainer-21h1g6jU > input',
            "10")
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.scrollable-2CTvqFKf > div > div:nth-child(4) > div > div > span > span"
        )
        await page.click(
            "#overlap-manager-root > div > div > div:nth-child(2) > div > span > div.dropdownMenu-1zfqRRWX.menuWrap-g78rwseC > div > div > div:nth-child(3) > div > div"
        )
        await page.click(
            "#overlap-manager-root > div > div > div.dialog-2AogBbC7.dialog-2cMrvu9r.dialog-UM6w7sFp.rounded-UM6w7sFp.shadowed-UM6w7sFp > div > div.footer-KW8170fm > div.buttons-KW8170fm > span > button > span"
        )

        await page.hover(
            "#widget-container > div.js-rootresizer__contents > div > div > div.chart-container-border > div > table > tr:nth-child(2) > td:nth-child(3) > div > div > div > div.gear-1DJMiIgd"
        )

        BB_UP = await page.evaluate('''() => {
        var yolo = document.evaluate("/html/body/div[2]/div/div/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div", document, null, XPathResult.STRING_TYPE, null)
        return yolo.stringValue
      }''')
        #print(BB_UP)
        BB_DOWN = await page.evaluate('''() => {
        var yolo = document.evaluate("/html/body/div[2]/div/div/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/div", document, null, XPathResult.STRING_TYPE, null)
        return yolo.stringValue
      }''')
        #print(BB_DOWN)

        WMA_5H = await page.evaluate('''() => {
        var yolo = document.evaluate("/html/body/div[2]/div/div/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div/div", document, null, XPathResult.STRING_TYPE, null)
        return yolo.stringValue
      }''')
        #print(WMA_5H)

        WMA_5L = await page.evaluate('''() => {
        var yolo = document.evaluate("/html/body/div[2]/div/div/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div/div/div", document, null, XPathResult.STRING_TYPE, null)
        return yolo.stringValue
      }''')
        #print(WMA_5L)

        WMA_10H = await page.evaluate('''() => {
        var yolo = document.evaluate("/html/body/div[2]/div/div/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[5]/div[2]/div/div/div", document, null, XPathResult.STRING_TYPE, null)
        return yolo.stringValue
      }''')
        #print(WMA_10H)

        WMA_10L = await page.evaluate('''() => {
        var yolo = document.evaluate("/html/body/div[2]/div/div/div[1]/div/table/tr[1]/td[2]/div/div[1]/div[2]/div[2]/div[6]/div[2]/div/div/div", document, null, XPathResult.STRING_TYPE, null)
        return yolo.stringValue
      }''')
        #print(WMA_10L)

        #await asyncio.sleep(3)
        #await page.screenshot({'path': "ss.png"})
        await page.close()
    except:
        try:
            await page.close()
        except:
            print("Page already closed...")
        print("Skipped")
    return BB_UP, BB_DOWN, WMA_5H, WMA_5L, WMA_10H, WMA_10L


async def master(*pairs):
    for pair in pairs:
        time_frames = ['15', '60', '240']
        for time_frame in time_frames:
            BB_UP, BB_DOWN, WMA_5H, WMA_5L, WMA_10H, WMA_10L = await process_chart(
                pair, time_frame)

            if WMA_5H > BB_UP:
                webhook = DiscordWebhook(
                    url=webhook_url,
                    content=f'{pair} {time_frame} -> **WMA_5H > BB_UP**')
                webhook.execute()
            if WMA_10H > BB_UP:
                webhook = DiscordWebhook(
                    url=webhook_url,
                    content=f'{pair} {time_frame} -> **WMA_10H > BB_UP**')
                webhook.execute()
            if WMA_5L < BB_DOWN:
                webhook = DiscordWebhook(
                    url=webhook_url,
                    content=f'{pair} {time_frame} -> **WMA_5L < BB_DOWN**')
                webhook.execute()
            if WMA_10L < BB_DOWN:
                webhook = DiscordWebhook(
                    url=webhook_url,
                    content=f'{pair} {time_frame} -> **WMA_10L < BB_DOWN**')
                webhook.execute()


async def run():
    await start_chrome()
    task1 = asyncio.create_task(
        master("audcad", "audchf", "audjpy", "audnzd", "audusd", "cadchf",
               "cadjpy", "chfjpy", "cnhjpy", "euraud", "eurcad", "eurchf",
               "eurcnh", "eurgbp", "eurjpy", "eurnzd", "eurtry", "eurusd",
               "gbpaud", "gbpcad", "gbpchf", "gbpinr", "gbpjpy", "gbpnzd",
               "gbpusd", "nzdcad", "nzdchf", "nzdjpy", "nzdusd", "usdbrl",
               "usdcad", "usdchf", "ushcnh", "usdinr", "usdjpy", "usdmxn",
               "usdrub", "usdsgd", "usdthb", "usdtry", "usdzar", "xagusd",
               "xauinr", "xauusd"))
    await task1

while 0 < 1:
  asyncio.get_event_loop().run_until_complete(run())
