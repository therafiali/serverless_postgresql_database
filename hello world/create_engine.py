from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text


load_dotenv()

key = os.getenv("db_key")


USERNAME = "alex"
PASSWORD = "AbC123dEf"
HOST = "ep-cool-darkness-123456.us-east-2.aws.neon.tech"
DATABASE = "dbname"

conn_str = f'{key}'

engine = create_engine(conn_str)

# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS users (x int, y int)"))
    conn.execute(text("INSERT INTO users (x, y) VALUES (:x, :y)"),
                 [{'x': 1, "y": 1}, {'x': 2, "y": 2}],)
    conn.commit()