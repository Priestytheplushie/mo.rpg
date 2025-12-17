import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    exit()

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello! I am {bot.user.name}.')

if __name__ == "__main__":
    bot.run(TOKEN)