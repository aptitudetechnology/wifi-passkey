#!/usr/bin/env python3
import socket

def handle_client(conn, addr):
    data = conn.recv(1024)
    if not data:
        return

    if data == b"knock knock":
        conn.sendall(b"who's there?")
    else:
        print("Unexpected data received:", data)

    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('wpk-server.local', 12345))  # Replace with your desired port
        s.listen()
        print('Server listening on port 12345')

        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            handle_client(conn, addr)

if __name__ == "__main__":
    start_server()
