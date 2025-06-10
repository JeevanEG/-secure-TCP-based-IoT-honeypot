# -secure-TCP-based-IoT-honeypot
# 🛡️ IoT Honeypot Attacker Logger

A secure, TCP-based IoT honeypot system that detects and logs malicious payloads sent to a simulated IoT device. It features AES-based encryption, attacker IP spoofing, and a live dashboard to analyze attack behavior.

---

## 📌 Features

- Simulates a fake vulnerable IoT service.
- Encrypted TCP communication using Fernet (AES).
- Logs attacker IPs, commands, and timestamps.
- Real-time visualization with a Streamlit dashboard.
- Supports multi-client attack simulations.
- Safe sandbox: no real system is compromised.

---

## 🧠 Architecture

- **Server:** Accepts and decrypts commands, logs data, responds with fake system banners.
- **Client:** Mimics attacker, encrypts and sends commands.
- **Encryption:** AES-128 symmetric encryption using `cryptography.fernet`.
- **Logger:** Logs data to both SQLite and CSV.
- **Dashboard:** Visualizes logs using Streamlit.

---

## 🖥️ Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
Libraries used:

cryptography

streamlit

pandas

sqlite3 (built-in)

requests

🚀 Getting Started
1. Start the Honeypot Server
bash
Copy
Edit
python server.py
2. Launch a Simulated Attacker (Client)
bash
Copy
Edit
python client.py
You’ll be prompted to enter:

Server IP (e.g., 127.0.0.1 for localhost)

A fake attacker IP (e.g., 51.140.123.1)

A command to simulate (e.g., ls, whoami, etc.)

3. View Real-Time Dashboard
bash
Copy
Edit
streamlit run app.py
🛠️ Example Attack Simulation
bash
Copy
Edit
Enter Server IP (WSL2 IP): 127.0.0.1
Enter fake attacker IP: 51.140.123.1
Enter command: whoami
📊 Dashboard Features
Filter logs by attacker IP, payload, and country.

Visualize:

📈 Attack frequency by IP

🌍 Attacks by country

🕒 Attacks over time

Download logs as CSV

📁 Project Structure
graphql
Copy
Edit
.
├── app.py              # Streamlit dashboard
├── client.py           # Simulated attacker client
├── server.py           # Honeypot server
├── encryption.py       # Encryption/decryption using Fernet
├── logger.py           # Log handler (SQLite and CSV)
├── honeypot_core.py    # (Handles fake OS responses) ← ADD THIS FILE
├── honeypot_logs.db    # SQLite log DB (excluded via .gitignore)
├── honeypot_logs.csv   # CSV log file (optional)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
🔐 Security Features
AES encryption for secure communication.

Fake IP injection for simulating geographic variation.

Logs attacker IPs, payloads, and timestamps.

No real services are exposed — everything is sandboxed.

📝 License
This project is intended for educational and research purposes only. No part of this system should be deployed in a live or production environment without proper review and modification.

🙋 Author
Jeevan EG
School of Computer Science
RV University

Track attack sources by country.

Plot attack frequency over time.

Download logs as CSV.
