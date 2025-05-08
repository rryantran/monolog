from discord import Embed, Interaction, app_commands
from discord.ext import commands
from db import insert_user, fetch_user
from visual.colors import dark_purple


class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setup")
    async def setup(self, interaction: Interaction):
        """Set up a user's journal"""

        discord_id = interaction.user.id

        if fetch_user(discord_id).data:
            embed = Embed(
                title="Journal Setup",
                description="Your journal is already set up.",
                color=dark_purple)

            await interaction.response.send_message(embed=embed)
            return

        insert_user(discord_id)

        embed = Embed(
            title="Journal Setup",
            description="Your journal has been set up.",
            color=dark_purple
        )

        await interaction.response.send_message(embed=embed)
        return


async def setup(bot):
    """Add the Setup cog"""

    await bot.add_cog(Setup(bot))
