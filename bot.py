import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def cool(ctx):
    
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
        




@bot.command()
async def mem(ctx):
    liste = os.listdir("img/images")
    rastgelemem = random.choice(liste)
    with open(f"img/images/{rastgelemem}", "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def destek(ctx):
    tavsiye = ["Geri dönüşüm yapmak için belli atıkları geri dönüşüm kutularına atabilirsin", "Güneş enerjisi ile çalışan araçlar tercih edebilirsin", "Çöpünü yere atmak yerine çöp kutularını kullanabilirsin"]
    await ctx.send(random.choice(tavsiye))


@bot.command()
async def plastik(ctx):
    await ctx.send("Plastik, mavi kutulara atılır")

@bot.command()
async def cam(ctx):
    await ctx.send("Cam, yeşil veya beyaz renkli kutulara atılır")

@bot.command()
async def paper(ctx):
    await ctx.send("Kağıt, mavi renkli kutulara atılır")

@bot.command()
async def karton(ctx):
    await ctx.send("Karton, mavi renkli kutulara atılır")

@bot.command()
async def mavi(ctx):
    await ctx.send("Mavi renkli kutulara kağıt, karton, plastik, metal ve kompozit atılır.")

@bot.command()
async def yesil(ctx):
    await ctx.send("Yeşil renkli kutulara camdan yapılmış ürünler atılır.")

@bot.command()
async def kirmizi(ctx):
    await ctx.send("Kırmızı renkli kutulara tıbbi atıklar atılır.")


























bot.run("token")
