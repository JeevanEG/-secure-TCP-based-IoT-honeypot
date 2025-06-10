import sqlite3
import csv
from datetime import datetime
import os

DB_FILE = "honeypot_logs.db"
CSV_FILE = "honeypot_logs.csv"

def log_attempt(ip, payload):
    timestamp = datetime.now().isoformat()

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            Timestamp TEXT,
            Attacker_IP TEXT,
            Payload TEXT
        )
    ''')
    c.execute('INSERT INTO logs (Timestamp, Attacker_IP, Payload) VALUES (?, ?, ?)', (timestamp, ip, payload))
    conn.commit()
    conn.close()

    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Attacker_IP", "Payload"])
        writer.writerow([timestamp, ip, payload])
