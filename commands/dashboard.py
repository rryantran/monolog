from discord import Embed, Interaction, app_commands
from discord.ext import commands
from visual.colors import dark_purple
from db import fetch_entries


class Dashboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="dashboard")
    async def dashboard(self, interaction: Interaction):
        """View journal dashboard"""

        discord_id = interaction.user.id

        embed = Embed(
            title="Dashboard",
            color=dark_purple,
        )

        embed.add_field(
            name="Number of Entries",
            value=f"{fetch_entries(discord_id).count} entries written",
            inline=False,
        )

        await interaction.response.send_message(embed=embed)
        return


async def setup(bot):
    """Add the Dashboard cog"""

    await bot.add_cog(Dashboard(bot))
