#!/usr/bin/env python3
import socket

#echo server example
HOST = '127.0.0.1'
PORT = 65432

try:
    #create socket object, AF_INET: IPv4 address type, SOCK_STREAM: tcp connection type 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    
        #bind socket to address and port, must be new connection
        sock.bind((HOST, PORT))
        #enable server to accept connections
        sock.listen()
        
        #wait for incoming connections to accept
        #return tuple with new socket and address of client
        connection, address = sock.accept()
        
        #receive data from client
        with connection:
            print('Address: {}'.format(address))
            while True:
                data = connection.recv(1024)
                #if connection.recv() return empty byte object
                #the connection is closed
                if not data: break
                #echo data client sends
                connection.sendall(data)

except socket.error as e:
    print('connection error: {}'.format(e.args()))


