from discord import Embed
from discord.ext import commands
from db import fetch_user, insert_entry, fetch_entries, fetch_entry_dates
from views.date_filter import DateFilterView
from visual.colors import dark_purple


class Entry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add")
    async def add_entry(self, ctx, *, entry):
        """Add a new journal entry"""

        discord_id = ctx.author.id

        if not fetch_user(discord_id).data:
            embed = Embed(
                title="Journal Setup",
                description="Your journal is not set up.\n\nTo set up your journal, use the command `.setup`",
                color=dark_purple,
            )

            await ctx.send(embed=embed)
            return

        insert_entry(discord_id, entry,
                     ctx.message.created_at.date().isoformat())

        embed = Embed(
            title="Entry Added",
            description="Your journal entry has been added.",
            color=dark_purple,
        )

        embed.add_field(name="Entry", value=f"```{entry}```", inline=False)

        await ctx.send(embed=embed)
        return

    @commands.command(name="view")
    async def view_entries(self, ctx):
        """View journal entries"""

        discord_id = ctx.author.id

        if not fetch_user(discord_id).data:
            embed = Embed(
                title="Journal Setup",
                description="Your journal is not set up.\n\nTo set up your journal, use the command `.setup`",
                color=dark_purple,
            )

            await ctx.send(embed=embed)
            return

        entries = fetch_entries(discord_id).data

        if not entries:
            embed = Embed(
                title="Entries",
                description="You have no journal entries.",
                color=dark_purple,
            )

            await ctx.send(embed=embed)
            return

        dates = fetch_entry_dates(discord_id).data

        embed = Embed(
            title="Entries",
            description="Select a date to view your entries.",
            color=dark_purple,
        )

        await ctx.send(embed=embed, view=DateFilterView(dates, entries))
        return


async def setup(bot):
    """Add the Entry cog"""

    await bot.add_cog(Entry(bot))
