import os
import asyncio
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands

load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = commands.Bot(command_prefix=".", intents=intents)


async def load_cogs():
    """Load all cogs"""

    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            try:
                await bot.load_extension(f"commands.{filename[:-3]}")
                print(f"Loaded cog: {filename[:-3]}")
            except Exception as e:
                print(f"Failed to load {filename[:-3]} cog: {e}")


@bot.event
async def on_ready():
    """Register slash commands"""
    try:
        await bot.tree.sync()
        print(f"{bot.user.name} is online!")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(load_cogs())
    except Exception as e:
        print(f"Failed to load cogs: {e}")

    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        print(f"Failed to run bot: {e}")
