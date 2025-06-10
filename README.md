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

```bash
pip install -r requirements.txt
Libraries used:

cryptography

streamlit

pandas

sqlite3 (built-in)

requests

🚀 Getting Started
Start the server:

bash
Copy
Edit
python server.py
Run a simulated attacker (client):

bash
Copy
Edit
python client.py
Launch the dashboard:

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
Filter logs by IP, payload, or country.

Visualize attack frequency by IP.

Track attack sources by country.

Plot attack frequency over time.

Download logs as CSV.
