import os
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up intents
intents = Intents.default()
intents.dm_messages = True

# Set up commands
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """Print a message when the bot is ready"""

    print(f"monolog activated!")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
