import socket
import json
import time

PORT = 6001
LOG_FILE = "chat_log.txt"

def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}

while True:
    action = input("Enter Command (Users, Chat, History): ").lower()

    if action == "users":
        users = load_users()
        now = time.time()
        for ip, info in users.items():
            delta = now - info["timestamp"]
            status = "Online" if delta <= 10 else "Away"
            print(f"{info['username']} ({status}) – {ip}")

    elif action == "chat":
        users = load_users()
        name = input("Select user for chat (username): ")
        ip = None
        for k, v in users.items():
            if v["username"] == name:
                ip = k
                break
        if not ip:
            print("User not found.")
            continue

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((ip, PORT))
            msg = input("Message: ")
            client.send(json.dumps({"unencrypted message": msg}).encode())
            with open(LOG_FILE, "a") as f:
                f.write(f"{time.ctime()} | {name} | SENT | {msg}\n")

        except Exception as e:
            print("Connection Error:", e)
        client.close()

    elif action == "history":
        with open(LOG_FILE, "r") as f:
            print(f.read())

    else:
        print("Try again.")
