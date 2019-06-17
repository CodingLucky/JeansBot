import discord.ext
from discord.ext import commands
from discord.ext.commands import bot
import tracemalloc
from discord import *

tracemalloc.start()
bot = commands.Bot(command_prefix='!', description='BTW I USE LINUX MINT XFCE')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



@bot.event
async def on_ready():
    print("Everything's all ready to go~")

on_ready()

@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@bot.command()
async def math(ctx):
    await ctx.send("Hier, ein Taschenrechner mit Python als Basis: https://github.com/CodingLucky/TermCalc (Wozu brauch man denn nen Tachenrechner in Discord?")


@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Einen schönen Guten Tag!")

@bot.command()
async def jean(ctx):
    await ctx.send(":smiley: :wave: Linux Guides ist toll!")

@bot.command()
async def arch(ctx):
    await ctx.send("Die offizielle deutsche Arch Linux Website: https://www.archlinux.de/ "
                   
                    "Die Installationsanleitung: https://wiki.archlinux.org/index.php/Installation_guide (engl.) ")

@bot.command()
async def essen(ctx):
    await ctx.send(":entesusssauer:")

@bot.command()
async def mint(ctx):
    await ctx.send("Du willst eine tolle einsteigerfreundliche Linuxdistribution testen? Hier: https://linuxmint.com/ "
                   
                   "Für leistungsschwache PCs empfiehlt sich der XFCE Desktop.")

@bot.command()
async def cat(ctx):
    await ctx.send("Katzen sind toll, stimmts?")

@bot.command()
async def prank(ctx):
    await ctx.send("https://fckaf.de/spp")

@bot.command()
async def minetest(ctx):
    await ctx.send("Jean hat einen Minetest-Server, hier der Discord: https://discord.gg/pyazAyY")

@bot.command()
async def kde(ctx):
    await ctx.send("KDE ist klasse!, bestätigt von GB_2, Rioluu, Einsamer Geist und mir!")

@bot.command()
async def youtube(ctx):
    await ctx.send("Jeans YouTubekanal: https://www.youtube.com/channel/UCHZyqB9qHGGGw5QeRVEbQDg")

bot.remove_command('help')

@bot.command()
async def help(ctx):
    await ctx.send("Bitte nutze !hilfe")

@bot.command()
async def hilfe(ctx):
    embed = discord.Embed(title="LinuxGuides ServerBot", description="Als Prefix wird ! genutzt", color=0xeee657)

    embed.add_field(name="!math", value="Link zu einem TerminalTaschenrechner, basierend auf Python", inline=False)
    embed.add_field(name="!greet", value="Ich grüße dich!!!", inline=False)
    embed.add_field(name="!cat", value="Die WWahrheit!", inline=False)
    embed.add_field(name="!prank", value="Lass dich überraschen!", inline=False)
    embed.add_field(name="!hilfe", value="Hilfe.", inline=False)
    embed.add_field(name="!minetest", value="Jeans Minetestserver.", inline=False)
    embed.add_field(name="!youtube", value="Jeans YouTubekanal.", inline=False)
    embed.add_field(name="!help", value="Hilfe.", inline=False)
    embed.add_field(name="!mint", value="Infos zur Linuxdistribution Linux Mint.", inline=False)
    embed.add_field(name="!arch", value="BTW WER NUTZT HIER ARCH! :)", inline=False)
    embed.add_field(name="!essen", value="Pekingente, die war wohl gut!", inline=False)
    embed.add_field(name="!kde", value="Der beste Desktop weit und breit", inline=False)

    await ctx.send(embed=embed)
bot.run('TOKEN')
