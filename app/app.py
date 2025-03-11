from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = "postgres"
DB_NAME = os.getenv("POSTGRES_DB", "mydatabase")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")

def connect_db():
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
        return conn
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    conn = connect_db()
    if isinstance(conn, str):
        return f"Database connection error: {conn}"
    return "Connected to PostgreSQL!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
