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
