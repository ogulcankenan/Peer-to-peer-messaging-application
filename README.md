# Peer-to-Peer Messaging App

This project is a simple Python-based peer-to-peer messaging application that enables two computers on the same network to communicate directly. It uses UDP broadcast for peer discovery and direct socket communication for message exchange.

## 🚀 Features

- Peer discovery via UDP broadcast
- Message sending and receiving between two PCs
- Simple user tracking with `users.json`
- Chat log storage
- Separate initiator and responder modules

## 🗂️ Project Structure

| File | Description |
|------|-------------|
| `chat_initiator.py` | Starts a chat with a selected peer |
| `chat_responder.py` | Listens and responds to incoming messages |
| `peer_discovery.py` | Finds peers on the local network |
| `service_announcer.py` | Announces the service to the network |
| `users.json` | Stores known users and timestamps (can be regenerated) |
| `chat_log.txt` | Stores message logs (plain text) |

## 🧰 Requirements

- Python 3.7 or above
- No external libraries required (uses built-in `socket`, `json`, etc.)

## ⚙️ How to Run

Open a terminal in the project folder and follow these steps:

1. Discover peers:
   python peer_discovery.py

2. Announce your service:
   python service_announcer.py

3. To start a chat:
python chat_initiator.py

4. To respond to incoming messages:
python chat_responder.py

# Other notes 

In service_announcer.py you must write your own IP Adress in BROADCAST_IP

