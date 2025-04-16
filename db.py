import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
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


def fetch_entries(discord_id, number: str):
    """Fetch a number of journal entries from the database"""

    if number == "all":
        response = (
            db.table("entries")
            .select("*")
            .eq("discord_id", discord_id)
            .order("date", desc=True)
            .execute()
        )
    else:
        response = (
            db.table("entries")
            .select("*")
            .eq("discord_id", discord_id)
            .order("date", desc=True)
            .limit(int(number))
            .execute()
        )

    return response
