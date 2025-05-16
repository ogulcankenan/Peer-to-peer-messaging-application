import socket
import json
import time
import threading

PORT = 6000
users = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

def write_users():
    with open("users.json", "w") as f:
        json.dump(users, f)

while True:
    data, addr = sock.recvfrom(1024)
    ip = addr[0]
    try:
        payload = json.loads(data.decode())

        
        if not isinstance(payload, dict) or "username" not in payload:
            raise ValueError("Geçersiz veri formatı")

        username = payload["username"]
        timestamp = time.time()

        if ip not in users:
            print(f"{username} is online ({ip})")

        users[ip] = {"username": username, "timestamp": timestamp}
        write_users()

    except Exception as e:
        print("Error:", e)
