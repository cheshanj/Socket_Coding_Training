#!/usr/bin/env python3

import socket

#Define loopback IP | Only in this case as an example
HOST = '127.0.0.1'

#Define the port
PORT = 65423

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as mySocket:
    mySocket.connect((HOST,PORT))
    mySocket.sendall(b'Hello from client!!')
    data = mySocket.recv(1024)

    print('Received!!', repr(data))