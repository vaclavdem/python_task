import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

conn = psycopg.connect(
    dbname=os.getenv("DBNAME"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
)

cursor = conn.cursor()
