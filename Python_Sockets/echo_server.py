#!/usr/bin/env python3

#imprting the socket library
import socket
#socket.getaddrinfo('127.0.0.1','8080')

#Define loopback IP | Only in this case as an example
HOST = '127.0.0.1'

#Define the port
PORT = 65423

#Define AMT_DATA
AMT_DATA = 64

#Socekt created the socket() <-function
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as mySocket:
    mySocket.bind((HOST, PORT))
    mySocket.listen()
    conn, addr = mySocket.accept()
    #Bind the socket with proper IP and a port with bind()

#Listning the socket with listen()
    
#Blocking mode with accept()

#conn, addr = mySocket.accept()

    with conn: 
        print("Connected by: " , addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

#Send and receive data