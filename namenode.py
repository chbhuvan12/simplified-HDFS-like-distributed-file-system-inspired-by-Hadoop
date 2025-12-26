import socket
import threading
import uuid
from config import DATANODES, REPLICATION_FACTOR

# filename -> block_id
files = {}

# block_id -> [datanodes]
blocks = {}

def handle_client(conn):
    msg = conn.recv(1024).decode()
    cmd, filename = msg.split()

    if cmd == "PUT":
        block_id = str(uuid.uuid4())
        chosen_nodes = list(DATANODES.keys())[:REPLICATION_FACTOR]

        files[filename] = block_id
        blocks[block_id] = chosen_nodes

        reply = f"{block_id} {' '.join(chosen_nodes)}"
        conn.send(reply.encode())

    elif cmd == "GET":
        block_id = files.get(filename)
        nodes = blocks.get(block_id)
        conn.send(f"{block_id} {nodes[0]}".encode())

    conn.close()

def start():
    s = socket.socket()
    s.bind((NAMENODE_HOST, NAMENODE_PORT))
    s.listen()
    print("NameNode running...")

    while True:
        conn, _ = s.accept()
        threading.Thread(target=handle_client, args=(conn,)).start()

if __name__ == "__main__":
    from config import NAMENODE_HOST, NAMENODE_PORT
    start()
