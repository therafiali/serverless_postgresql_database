from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text


load_dotenv()

key = os.getenv("db_key")

conn_str = f'{key}'

engine = create_engine(conn_str, echo=True)