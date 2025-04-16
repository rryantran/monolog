from discord.ext import commands
from discord import Embed
from db import fetch_user, insert_entry, fetch_entries


class Entry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add")
    async def add_entry(self, ctx, *, entry):
        """Add a new journal entry"""
        discord_id = ctx.author.id

        if not fetch_user(discord_id).data:
            embed = Embed(
                title="Setup",
                description="Your journal is not set up.\n\nTo set up your journal, use the command `.setup`",
            )

            await ctx.send(embed=embed)
            return

        insert_entry(discord_id, entry,
                     ctx.message.created_at.date().isoformat())

        embed = Embed(
            title="Add Entry",
            description="Your journal entry has been added.",
        )

        embed.add_field(name="Entry", value=f'```{entry}```', inline=False)

        await ctx.send(embed=embed)
        return

    @commands.command(name="view")
    async def view_entries(self, ctx, number: str = "5"):
        """View a number of or all journal entries"""
        discord_id = ctx.author.id

        if not fetch_user(discord_id).data:
            embed = Embed(
                title="Setup",
                description="Your journal is not set up.\n\nTo set up your journal, use the command `.setup`",
            )

            await ctx.send(embed=embed)
            return

        entries = fetch_entries(discord_id, number).data

        if not entries:
            embed = Embed(
                title="View Entries",
                description="You have no journal entries.",
            )

            await ctx.send(embed=embed)
            return

        embed = Embed(
            title="View Entries",
            description="Here are your journal entries:",
        )

        for entry in entries:
            embed.add_field(
                name=f"Entry {entry["id"]} - {entry["date"]}",
                value=f'```{entry["content"]}```',
                inline=False,
            )

        await ctx.send(embed=embed)
        return


async def setup(bot):
    """Add the Entry cog"""

    await bot.add_cog(Entry(bot))
