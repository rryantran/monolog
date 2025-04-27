import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("SUPABASE_URL")
DB_KEY = os.getenv("SUPABASE_KEY")

db = create_client(DB_URL, DB_KEY)


def insert_user(discord_id):
    """Insert a new user into the database"""

    data = {
        "discord_id": discord_id,
    }

    response = (
        db.table("users").
        insert(data).
        execute()
    )

    return response


def fetch_user(discord_id):
    """Fetch a user from the database"""

    response = (
        db.table("users")
        .select("*")
        .eq("discord_id", discord_id)
        .execute()
    )

    return response


def insert_entry(discord_id, content, date):
    """Insert a new journal entry into the database"""

    data = {
        "discord_id": discord_id,
        "content": content,
        "date": date,
    }

    response = (
        db.table("entries").
        insert(data).
        execute()
    )

    return response


def fetch_entries(discord_id):
    """Fetch journal entries from the database"""

    response = (
        db.table("entries")
        .select("*", count="exact")
        .eq("discord_id", discord_id)
        .order("date", desc=True)
        .execute()
    )

    return response


def fetch_entry_dates(discord_id):
    """Fetch journal entry dates from the database"""

    # Fetch using stored procedure (in Supabase SQL Editor)
    response = (
        db.rpc("get_entry_counts_by_date", {
            "discord_id_param": discord_id}).execute()
    )

    return response
