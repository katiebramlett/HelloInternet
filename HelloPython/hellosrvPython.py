#!/usr/bin/env python3

import socket

<<<<<<< HEAD
HOST = "127.0.1.0"  # Listen on all interfaces
=======
HOST = "127.0.0.1"  # Listen on all interfaces
>>>>>>> ed0e8fc6a1ddc3d8e2b192b914f9a10e1d6c582f
PORT = 8080
msg = "Goodbye in Python"

print("Starting Python hellosrv")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print("Connection from ", addr)
            data = conn.recv(1024)
            print(data.decode())
            conn.sendall(msg.encode())
            conn.close()
