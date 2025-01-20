# app_v3.py
from flask import Flask, request
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    dbname="yourdb",
    user="youruser",
    password="yourpassword",
    host="db",  # Docker service name
    port="5432"
)

@app.route('/')
def log_access():
    cur = conn.cursor()
    cur.execute("INSERT INTO access_logs (timestamp, ip) VALUES (%s, %s)", 
                (datetime.now(), request.remote_addr))
    conn.commit()
    cur.close()
    return "Access logged!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
