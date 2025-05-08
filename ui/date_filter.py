from discord import Embed, SelectOption
from discord.ui import Select, View
from visual.colors import dark_purple


class DateFilter(Select):
    def __init__(self, dates, entries):
        self.entries = entries

        # Create list of SelectOption objects from entry dates
        options = [SelectOption(label=date["date"], value=date["date"],
                                description=f"Number of Entires: {date["entry_count"]}") for date in dates]

        # Inhereit from Select
        super().__init__(
            placeholder="Select a date",
            options=options,
        )

    async def callback(self, interaction):
        """Callback for when the select is changed"""

        selected_date = self.values[0]

        # Filter entries based on selected date
        entries = [
            entry for entry in self.entries if entry["date"] == selected_date]

        embed = Embed(
            title=f"Entries for {selected_date}",
            color=dark_purple,
        )

        for i, entry in enumerate(entries):
            embed.add_field(
                name=f"Entry {i + 1}",
                value=f"```{entry["content"]}```",
                inline=False,
            )

        await interaction.response.edit_message(embed=embed)
        return


class DateFilterView(View):
    def __init__(self, dates, entries):
        # Inherit from View
        super().__init__()
        self.add_item(DateFilter(dates, entries))
