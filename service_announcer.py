import socket
import json
import time


BROADCAST_IP = ''  #write your IP adress here
PORT = 6000

username = input("Please enter your username : ")
my_ip = socket.gethostbyname(socket.gethostname())

message = json.dumps({"username": username})
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    sock.sendto(message.encode(), (BROADCAST_IP, PORT))
    print(f"[BROADCAST] {username} is online ({my_ip})")
    time.sleep(8)
