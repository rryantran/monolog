from discord import Embed, Interaction, app_commands
from discord.ext import commands
from db import fetch_user, fetch_entries, fetch_entry_dates
from ui.date_filter import DateFilterView
from ui.entry_modal import EntryModal
from visual.colors import dark_purple


class Entry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="add")
    async def add_entry(self, interaction: Interaction):
        """Add a new journal entry"""

        discord_id = interaction.user.id

        if not fetch_user(discord_id).data:
            embed = Embed(
                title="Journal Setup",
                description="Your journal is not set up.\n\nTo set up your journal, use the command `.setup`",
                color=dark_purple,
            )

            await interaction.response.send_message(embed=embed)
            return

        await interaction.response.send_modal(EntryModal(discord_id))
        return

    @app_commands.command(name="view")
    async def view_entries(self, interaction: Interaction):
        """View journal entries"""

        discord_id = interaction.user.id

        if not fetch_user(discord_id).data:
            embed = Embed(
                title="Journal Setup",
                description="Your journal is not set up.\n\nTo set up your journal, use the command `.setup`",
                color=dark_purple,
            )

            await interaction.response.send_message(embed=embed)
            return

        entries = fetch_entries(discord_id).data

        if not entries:
            embed = Embed(
                title="Entries",
                description="You have no journal entries.",
                color=dark_purple,
            )

            await interaction.response.send_message(embed=embed)
            return

        dates = fetch_entry_dates(discord_id).data

        embed = Embed(
            title="Entries",
            description="Select a date to view your entries.",
            color=dark_purple,
        )

        await interaction.response.send_message(embed=embed, view=DateFilterView(dates, entries))
        return


async def setup(bot):
    """Add the Entry cog"""

    await bot.add_cog(Entry(bot))
