import requests

def get_fake_banner():
    return "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3"

def handle_payload(data):
    command = data.decode(errors='ignore').strip().lower()

    if command == "whoami":
        return b"root"
    elif command == "uname -a":
        return b"Linux honeypot 5.15.90-mock #1 SMP Thu Jan 1 00:00:00 UTC 2025 x86_64 GNU/Linux"
    elif command.startswith("ls"):
        return b"secret.txt\npasswd_backup\nhoneypot.py\nlogs.log"
    elif command.startswith("cat"):
        return b"Access denied: permission issue or file does not exist."
    elif command.startswith("cd"):
        return b"Directory changed."
    elif command.startswith("sudo"):
        return b"Permission denied: user is not in the sudoers file."
    elif "passwd" in command:
        return b"root:x:0:0:root:/root:/bin/bash\nuser:x:1000:1000:User:/home/user:/bin/bash"
    elif command == "netstat -tulnp":
        return b"""
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1234/sshd
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      4567/apache2
"""
    elif "wget" in command or "curl" in command:
        return b"Error: Network unreachable."
    elif "rm" in command:
        return b"Permission denied"
    elif command == "exit":
        return b"Goodbye."
    else:
        return f"Command '{command}' not recognized".encode()


def get_country_from_ip(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
        data = res.json()
        return data.get("country", "Unknown")
    except:
        return "Unknown"
