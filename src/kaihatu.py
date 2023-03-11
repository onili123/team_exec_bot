import discord
from discord.ext import commands
import discord.app_commands
import os
import random

TOKEN = os.getenv("DISCORD_TOKEN")

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


@bot.command()
async def 占い(ctx):
    uranai = ["大吉","中吉","吉","末吉"]
    choice = random.choice(uranai)
    await ctx.send(choice)

bot.run(TOKEN)
