import socket
from encryption import encrypt, decrypt

HOST = input("Enter Server IP (WSL2 IP): ").strip()
PORT = 9090

FAKE_IP = input("Enter fake attacker IP (for log simulation): ").strip()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(encrypt(f"FAKE_IP:{FAKE_IP}".encode()))

    banner = decrypt(s.recv(4096)).decode()
    print(f"[+] Server says: {banner}")

    while True:
        cmd = input("Enter command: ")
        s.send(encrypt(cmd.encode()))
        if cmd == "exit":
            break
        response = decrypt(s.recv(4096)).decode()
        print(f"[Server] {response}")
