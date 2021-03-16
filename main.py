import discord
from discord.ext import commands, tasks
from browser import *
import os

client = commands.Bot(command_prefix='.')

@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command()
async def all(ctx, exchange, pair, time_frame, *studies1):
    t1 = asyncio.create_task(t(ctx, exchange, pair, time_frame))

    if "m" in time_frame:
        new_time_frame = int(time_frame.replace("m", ""))
    elif "h" in time_frame:
        new_time_frame = int(time_frame.replace("h", "")) * 60

    if len(studies1) == 0:
        t2 = asyncio.create_task(c(ctx, exchange, pair, new_time_frame))
    else:
        t2 = asyncio.create_task(
            c(ctx, exchange, pair, new_time_frame, *studies1))
    await t1
    await t2


@client.command()
async def allh(ctx):
    help = ".all  <**exchange**>  <**pair**>  <**time_frame**>  <***Opt.***[**studies**]>"
    await ctx.send(help)


@client.command()
async def s(ctx, order, to_show, *columns):
    await screener_runner(order, to_show, columns)
    await ctx.send(file=discord.File("s.png"))
@client.command()
async def sh(ctx):
    help = ".s  <**order**>  <**ordering_of_which_column**>  <**columns**>"
    await ctx.send(help)


@client.command()
async def t(ctx, exchange, pair, time_frame, *theme):
    color = ""
    for i in theme:
        if i != "":
            color = "dark"
        else:
            color = "light"

    url = f'https://s.tradingview.com/embed-widget/technical-analysis/?locale=en#%7B%0A%20%20%22interval%22%3A%20%22{time_frame}%22%2C%0A%20%20%22width%22%3A%20%22500%22%2C%0A%20%20%22isTransparent%22%3A%20false%2C%0A%20%20%22height%22%3A%20%22500%22%2C%0A%20%20%22symbol%22%3A%20%22{exchange}%3A{pair}%22%2C%0A%20%20%22showIntervalTabs%22%3A%20true%2C%0A%20%20%22locale%22%3A%20%22en%22%2C%0A%20%20%22colorTheme%22%3A%20%22{color}%22%0A%7D'

    await take_screenshot_runner(url, "t.png", 500, 500)
    await ctx.send(file=discord.File('t.png'))
@client.command()
async def th(ctx):
  help = ".t  <**exchange**>  <**pair**>  <**time_frame**>  <***Opt.***[**theme**]"
  await ctx.send(help)


@client.command()
async def e(ctx, *theme):
    color = ""
    for i in theme:
        if i != "":
            color = "dark"
        else:
            color = "light"

    url = f"https://s.tradingview.com/embed-widget/events/?locale=en#%7B%0A%20%20%22colorTheme%22%3A%20%22{color}%22%2C%0A%20%20%22isTransparent%22%3A%20false%2C%0A%20%20%22width%22%3A%20%22510%22%2C%0A%20%20%22height%22%3A%20%22600%22%2C%0A%20%20%22locale%22%3A%20%22en%22%2C%0A%20%20%22importanceFilter%22%3A%20%22-1%2C0%2C1%22%2C%0A%20%20%22currencyFilter%22%3A%20%22USD%2CAUD%2CCAD%2CJPY%2CNZD%2CGBP%2CFRF%22%0A%7D"

    await take_screenshot_runner(url, "e.png", 600, 800)
    await ctx.send(file=discord.File('e.png'))
@client.command()
async def eh(ctx):
  help = ".e  <***Opt.***[**theme**]>"
  await ctx.send(help)

@client.command()
async def fcr(ctx, *theme):
    color = ""
    for i in theme:
        if i != "":
            color = "dark"
        else:
            color = "light"
    url = f'https://s.tradingview.com/embed-widget/forex-cross-rates/?locale=en#%7B%0A%20%20%22width%22%3A%20%22100%25%22%2C%0A%20%20%22height%22%3A%20%22500%22%2C%0A%20%20%22currencies%22%3A%20%5B%0A%20%20%20%20%22EUR%22%2C%0A%20%20%20%20%22USD%22%2C%0A%20%20%20%20%22JPY%22%2C%0A%20%20%20%20%22GBP%22%2C%0A%20%20%20%20%22CHF%22%2C%0A%20%20%20%20%22AUD%22%2C%0A%20%20%20%20%22CAD%22%2C%0A%20%20%20%20%22NZD%22%2C%0A%20%20%20%20%22CNY%22%0A%20%20%5D%2C%0A%20%20%22isTransparent%22%3A%20false%2C%0A%20%20%22colorTheme%22%3A%20%22{color}%22%2C%0A%20%20%22locale%22%3A%20%22en%22%0A%7D'

    await take_screenshot_runner(url, "fcr.png", 900, 900)
    await ctx.send(file=discord.File("fcr.png"))
@client.command()
async def fcrh(ctx):
    help = ".fcr  <***Opt.***[**theme**]>"
    await ctx.send(help)


@client.command()
async def fhm(ctx, *theme):
    color = ""
    for i in theme:
        if i != "":
            color = "dark"
        else:
            color = "light"
    url = f'https://s.tradingview.com/embed-widget/forex-heat-map/?locale=en#%7B%0A%20%20%22width%22%3A%20%22100%25%22%2C%0A%20%20%22height%22%3A%20%22500%22%2C%0A%20%20%22currencies%22%3A%20%5B%0A%20%20%20%20%22EUR%22%2C%0A%20%20%20%20%22USD%22%2C%0A%20%20%20%20%22JPY%22%2C%0A%20%20%20%20%22GBP%22%2C%0A%20%20%20%20%22CHF%22%2C%0A%20%20%20%20%22AUD%22%2C%0A%20%20%20%20%22CAD%22%2C%0A%20%20%20%20%22NZD%22%2C%0A%20%20%20%20%22CNY%22%0A%20%20%5D%2C%0A%20%20%22isTransparent%22%3A%20false%2C%0A%20%20%22colorTheme%22%3A%20%22{color}%22%2C%0A%20%20%22locale%22%3A%20%22en%22%0A%7D'

    await take_screenshot_runner(url, "fhm.png", 900, 900)
    await ctx.send(file=discord.File("fhm.png"))
@client.command()
async def fhmh(ctx):
    help = ".fhm  <***Opt.***[**theme**]>"
    await ctx.send(help)


@client.command()
async def f(ctx, exchange, pair, *theme):
    color = ""
    for i in theme:
        if i != "":
            color = "dark"
        else:
            color = "light"
    url = f'https://s.tradingview.com/embed-widget/financials/?locale=en#%7B%0A%20%20%22symbol%22%3A%20%22{exchange}%3A{pair}%22%2C%0A%20%20%22colorTheme%22%3A%20%22{color}%22%2C%0A%20%20%22isTransparent%22%3A%20false%2C%0A%20%20%22largeChartUrl%22%3A%20%22%22%2C%0A%20%20%22displayMode%22%3A%20%22regular%22%2C%0A%20%20%22width%22%3A%20%22100%25%22%2C%0A%20%20%22height%22%3A%20%221000%22%2C%0A%20%20%22locale%22%3A%20%22en%22%0A%7D'

    await take_screenshot_runner(url, "f.png", 800, 800)
    await ctx.send(file=discord.File("f.png"))
@client.command()
async def fh(ctx):
    help = ".f  <**exchange**>  <**pair**>  <***Opt.***[**theme**]>"
    await ctx.send(help)


@client.command()
async def p(ctx, exchange, pair, *theme):
    color = ""
    for i in theme:
        if i != "":
            color = "dark"
        else:
            color = "light"
    url = f'https://s.tradingview.com/embed-widget/symbol-profile/?symbol={exchange}%3A{pair}&colorTheme={color}'
    await take_screenshot_runner(url, "p.png", 600, 600)
    await ctx.send(file=discord.File("p.png"))
@client.command()
async def ph(ctx):
    help = ".p  <**exchange**>  <**pair**>  <***Opt.***[**theme**]>"
    await ctx.send(help)


@client.command()
async def c(ctx, exchange, pair, time_frame, *studies1):

    if "m" in str(time_frame):
        time_frame = int(time_frame.replace("m", ""))
    if "h" in str(time_frame):
        time_frame = int(time_frame.replace("h", "")) * 60

    studies = ""
    for i in studies1:
        if i != "":
            studies = studies + i + "%40tv-basicstudies%1F"

    url = f'https://s.tradingview.com/widgetembed/?frameElementId=tradingview_33e44&symbol={exchange}%3A{pair}&interval={time_frame}&hidetoptoolbar=1&symboledit=1&saveimage=0&toolbarbg=f1f3f6&studies={studies}&theme=light&style=1&timezone=Etc%2FUTC&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=en'

    await take_screenshot_runner(url, "c.png", 800, 600)
    await ctx.send(file=discord.File("c.png"))
@client.command()
async def ch(ctx):
    help = ".c  <**exchange**>  <**pair**>  <**time_frame**>  <***Opt.***[**studies**]>"
    await ctx.send(help)


####### HELP #######
@client.command()
async def h(ctx):
    help = ".s  ->  **Screener**\n.c  ->  **Chart**\n.t  ->  **Technical Analysis**\n.e  ->  **Upcoming Events**\n.f  ->  **Financials**\n.p  ->  **Company Profie**\n.fcr  ->  **Forex Cross Rate**\n.fhm  ->  **Forex Heat Map**\n"
    await ctx.send(help)



#######  EVENT  ######
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await start_chrome()

@client.event 
async def on_message(message):
  if message.author.bot: return
  if message.content.startswith('.'):
    await message.add_reaction('\N{THUMBS UP SIGN}')
  await client.process_commands(message)


@tasks.loop(seconds=60)
async def oop():
    print("Bot is running...")
@oop.before_loop
async def before():
    await client.wait_until_ready()

oop.start()






######   RUN   ######
client.run(os.getenv("BOT_TOKEN"))
