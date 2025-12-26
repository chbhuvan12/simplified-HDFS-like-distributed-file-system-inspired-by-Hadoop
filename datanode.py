import socket
import os
import sys

port = int(sys.argv[1])
data_dir = sys.argv[2]
os.makedirs(data_dir, exist_ok=True)

def start():
    s = socket.socket()
    s.bind(("localhost", port))
    s.listen()
    print(f"DataNode running on {port}")

    while True:
        conn, _ = s.accept()
        data = conn.recv(10_000_000)

        if data.startswith(b"WRITE"):
            _, block_id, content = data.split(b"|", 2)
            with open(f"{data_dir}/{block_id.decode()}", "wb") as f:
                f.write(content)
            conn.send(b"OK")

        elif data.startswith(b"READ"):
            _, block_id = data.split(b"|", 1)
            with open(f"{data_dir}/{block_id.decode()}", "rb") as f:
                conn.send(f.read())

        conn.close()

start()
