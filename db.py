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

    response = db.table("users").insert(data).execute()

    return response
