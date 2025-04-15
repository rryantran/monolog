import os
from dotenv import load_dotenv
from discord import Intents, DMChannel
from discord.ext import commands
from db import insert_user

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up intents
intents = Intents.default()
intents.message_content = True
intents.dm_messages = True

# Set up commands
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """Print a message when the bot is ready"""

    print(f"monolog activated!")


@bot.event
async def on_message(message):
    """Respond to hello message from user in DMs"""

    if isinstance(message.channel, DMChannel):
        if message.author != bot.user and message.content.lower() == "hello":
            insert_user(message.author.id)
            await message.channel.send("Hello! this is **monolog**, your journaling companion for Discord.")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
