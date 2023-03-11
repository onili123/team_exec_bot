import discord
from discord.ext import commands
import discord.app_commands

TOKEN = 'MTA4MzMzNzc0MDc4OTIyMzQ3NA.Gl_ni9.Eqasp5R_HpzELt3M_QXLC6lSdFqK1-yyLOlEGA'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='にゃん', intents=intents)





@bot.event
async def on_ready():
    print('Botが起動しましたにゃん！')


@bot.command()
async def なでる(ctx):
    await ctx.send(':cat: にゃーん')


@bot.command()
async def たたく(ctx):
    await ctx.send(':cat: うわーん')

bot.run(TOKEN)
