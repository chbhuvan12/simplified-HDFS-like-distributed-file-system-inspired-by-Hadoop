import socket
from config import *

def put(filename):
    nn = socket.socket()
    nn.connect((NAMENODE_HOST, NAMENODE_PORT))
    nn.send(f"PUT {filename}".encode())

    block_id, *nodes = nn.recv(1024).decode().split()
    nn.close()

    data = open(filename, "rb").read()

    for dn in nodes:
        host, port, _ = DATANODES[dn]
        s = socket.socket()
        s.connect((host, port))
        s.send(b"WRITE|" + block_id.encode() + b"|" + data)
        s.recv(1024)
        s.close()

    print("File uploaded successfully")

def get(filename):
    nn = socket.socket()
    nn.connect((NAMENODE_HOST, NAMENODE_PORT))
    nn.send(f"GET {filename}".encode())

    block_id, dn = nn.recv(1024).decode().split()
    nn.close()

    host, port, _ = DATANODES[dn]
    s = socket.socket()
    s.connect((host, port))
    s.send(b"READ|" + block_id.encode())
    data = s.recv(10_000_000)
    s.close()

    open("output_" + filename, "wb").write(data)
    print("File downloaded successfully")

if __name__ == "__main__":
    put("test.txt")
    get("test.txt")
