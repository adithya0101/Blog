from sqlalchemy import create_engine
# from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
class Config:
    # Flask secret key (used for session management, CSRF protection, etc.)
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")

    # Supabase credentials (optional if you're also using Supabase SDK)
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

    # SQLAlchemy database URI (this is for Supabase PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.getenv("SUPABASE_DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Recommended setting

    # Construct the SQLAlchemy connection string

    # Create the SQLAlchemy engine
    engine = create_engine(SUPABASE_URL)
    # If using Transaction Pooler or Session Pooler, we want to ensure we disable SQLAlchemy client side pooling -
    # https://docs.sqlalchemy.org/en/20/core/pooling.html#switching-pool-implementations
    # engine = create_engine(DATABASE_URL, poolclass=NullPool)

    # Test the connection
    try:
        with engine.connect() as connection:
            print("Connection successful!")
    except Exception as e:
        print(f"Failed to connect: {e}")