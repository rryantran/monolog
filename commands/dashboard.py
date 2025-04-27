from discord import Embed
from discord.ext import commands
from visual.colors import dark_purple
from db import fetch_entries


class Dashboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dashboard")
    async def dashboard(self, ctx):
        """View journal dashboard"""

        discord_id = ctx.author.id

        embed = Embed(
            title="Dashboard",
            color=dark_purple,
        )

        embed.add_field(
            name="Number of Entries",
            value=f"{fetch_entries(discord_id).count} entries written",
            inline=False,
        )

        await ctx.send(embed=embed)
        return


async def setup(bot):
    """Add the Dashboard cog"""

    await bot.add_cog(Dashboard(bot))
