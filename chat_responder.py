import socket
import json
import time

PORT = 6001
LOG_FILE = "chat_log.txt"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', PORT))
server.listen()

print("Mesaj bekleniyor...")

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    try:
        msg = json.loads(data)

        if "unencrypted message" in msg:
            print(f"[Mesaj] {msg['unencrypted message']}")
            with open(LOG_FILE, "a") as f:
                f.write(f"{time.ctime()} | {addr[0]} | RECEIVED | {msg['unencrypted message']}\n")

    except Exception as e:
        print("Error:", e)

    conn.close()
