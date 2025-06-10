import socket
from encryption import encrypt, decrypt
from honeypot_core import get_fake_banner, handle_payload
from logger import log_attempt
import threading

HOST = '0.0.0.0'
PORT = 9090

def handle_client(conn, addr):
    print(f"[+] Connection from {addr}")
    attacker_ip = addr[0]
    try:
        enc_ip = conn.recv(4096)
        fake_ip_msg = decrypt(enc_ip).decode(errors='ignore').strip()
        if fake_ip_msg.startswith("FAKE_IP:"):
            attacker_ip = fake_ip_msg.split(":")[1]
    except Exception as e:
        print(f"[-] Failed to get FAKE_IP: {e}")

    conn.send(encrypt(get_fake_banner()))

    while True:
        enc_data = conn.recv(4096)
        if not enc_data:
            break
        try:
            data = decrypt(enc_data)
            print(f"[*] {attacker_ip} sent: {data.decode(errors='ignore')}")
            log_attempt(attacker_ip, data.decode(errors='ignore'))
            response = handle_payload(data)
            conn.send(encrypt(response))
        except Exception as e:
            print(f"[!] Error handling data: {e}")
            break

    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[+] Listening on {HOST}:{PORT}")
    while True:
        conn,addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()