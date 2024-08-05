import sys
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Validate environment variables
if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]):
    print("Error: Missing one or more environment variables for database connection.")
    sys.exit(1)

# Create connection string
connection_string = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Create engine, connection, and metadata
engine = create_engine(connection_string, echo=True)
conn = engine.connect()
meta = MetaData()
