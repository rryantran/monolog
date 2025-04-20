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
            await bot.load_extension(f"commands.{filename[:-3]}")

if __name__ == "__main__":
    asyncio.run(load_cogs())
    bot.run(BOT_TOKEN)
