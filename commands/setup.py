from discord.ext import commands
from discord import Embed
from db import insert_user, fetch_user


class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setup")
    async def setup(self, ctx):
        """Set up a user's journal"""
        discord_id = ctx.author.id

        if fetch_user(discord_id).data:
            embed = Embed(
                title="Setup",
                description="Your journal is already set up.",
            )

            await ctx.send(embed=embed)
            return

        insert_user(discord_id)

        embed = Embed(
            title="Setup",
            description="Your journal has been set up.",
        )

        await ctx.send(embed=embed)
        return


async def setup(bot):
    """Add the Setup cog"""

    await bot.add_cog(Setup(bot))
