from discord import Embed, TextStyle
from discord.ui import Modal, TextInput
from db import insert_entry
from visual.colors import dark_purple


class EntryModal(Modal):
    def __init__(self, discord_id):
        # Inherit from Modal
        super().__init__(title="Add Entry")

        self.discord_id = discord_id
        self.entry = TextInput(
            label="Journal Entry",
            style=TextStyle.paragraph,
            placeholder="Write your journal entry here...",
            required=True,
            max_length=2000,
        )
        self.add_item(self.entry)

    async def on_submit(self, interaction):
        """Handle submission of new journal entry"""

        insert_entry(self.discord_id, self.entry.value,
                     interaction.created_at.date().isoformat())

        embed = Embed(
            title="Entry Added",
            description="Your journal entry has been added.",
            color=dark_purple,
        )

        embed.add_field(
            name="Entry", value=f"```{self.entry.value}```", inline=False)

        await interaction.response.send_message(embed=embed)
        return
