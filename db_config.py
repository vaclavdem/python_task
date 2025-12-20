import psycopg
import os
from dotenv import load_dotenv

conn = psycopg.connect(
    dbname=os.getenv('dbname'),
    user=os.getenv('user'),
    password=os.getenv('password'),
    host=os.getenv('host'),
    port=os.getenv('port')
)

print("CONNECTED")

cur = conn.cursor()