# -secure-TCP-based-IoT-honeypot
````markdown
# 🛡️ IoT Honeypot Attacker Logger

A secure, TCP-based IoT honeypot system that detects and logs malicious payloads sent to a simulated IoT device. It features AES-based encryption, attacker IP spoofing, and a live dashboard to analyze attack behavior.

## 📌 Features

- Simulates a fake vulnerable IoT service.
- Encrypted TCP communication using Fernet (AES).
- Logs attacker IPs, commands, and timestamps.
- Real-time visualization with a Streamlit dashboard.
- Supports multi-client attack simulations.
- Safe sandbox: no real system is compromised.

## 🧠 Architecture

- **Server:** Accepts and decrypts commands, logs data, responds with fake system banners.
- **Client:** Mimics attacker, encrypts and sends commands.
- **Encryption:** AES-128 symmetric encryption using `cryptography.fernet`.
- **Logger:** Logs data to both SQLite and CSV.
- **Dashboard:** Visualizes logs using Streamlit.

## 🖥️ Requirements

```bash
pip install -r requirements.txt
````

**Libraries used:**

* cryptography
* streamlit
* pandas
* sqlite3 (built-in)
* requests

## 🚀 Getting Started

### 1. Start the Honeypot Server

```bash
python server.py
```

### 2. Launch a Simulated Attacker (Client)

```bash
python client.py
```

You’ll be prompted to enter:

* Server IP (e.g., 127.0.0.1)
* A fake attacker IP (e.g., 51.140.123.1)
* A command to simulate (e.g., ls, whoami, etc.)

### 3. View Real-Time Dashboard

```bash
streamlit run app.py
```

## 🛠️ Example Attack Simulation

```bash
Enter Server IP (WSL2 IP): 127.0.0.1
Enter fake attacker IP: 51.140.123.1
Enter command: whoami
```

## 📊 Dashboard Features

* Filter logs by attacker IP, payload, and country.
* Visualize:

  * 📈 Attack frequency by IP
  * 🌍 Attacks by country
  * 🕒 Attacks over time
* Download logs as CSV

## 📁 Project Structure

```
.
├── app.py
├── client.py
├── server.py
├── encryption.py
├── logger.py
├── honeypot_core.py
├── requirements.txt
└── README.md
```

## 🔐 Security Features

* AES encryption for secure communication.
* Fake IP injection for simulating geographic variation.
* Logs attacker IPs, payloads, and timestamps.
* No real services are exposed — everything is sandboxed.

## 📝 License

This project is intended for educational and research purposes only. No part of this system should be deployed in a live or production environment without proper review and modification.

## 🙋 Author

**Jeevan EG**
School of Computer Science
RV University

```
```

Track attack sources by country.

Plot attack frequency over time.

Download logs as CSV.
