#!/usr/bin/env python3
import socket
import selectors
import types

def accept_wrapper(sock):
    
    global selector
    #accept client connection
    conn, addr = sock.accept()
    conn.setblocking(False)
    #create new dynamically typed object to store data
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    #allow for reading and writing events
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    #pass socket, events-mask and data to selector
    selector.register(conn, events, data=data)

def service_connection(key, mask):
    
    global selector
    sock = key.fileobj
    data = key.data
    #if socket is ready for reading
    if mask & selectors.EVENT_READ:
        rx = sock.recv(1024)
        if rx:
            #append to data.outb to be sent later
            data.outb += rx
        else:
            #client has closed socket so unregister and close
            selector.unregister(sock)
            sock.close()
            print('socket closed')
    #if socket is ready for writing
    if mask & selectors.EVENT_WRITE:
        #if outb is populated
        if data.outb:
            #echo to client
            sent = sock.send(data.outb)
            #remove bytes from outb buffer
            data.outb = data.outb[sent:]

#echo server example
HOST = '127.0.0.1'
PORT = 65432
'''
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
'''
selector = selectors.DefaultSelector()
socket_bind = (HOST, PORT)
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_sock:
        listen_sock.bind(socket_bind)
        listen_sock.listen()
        #prevent suspension of app
        listen_sock.setblocking(False)
        #register socket and wait for specified event
        selector.register(listen_sock, selectors.EVENT_READ, data=None)

        while True:
            #return list of tuples for each socket
            events = selector.select(timeout=None)
            for key, mask in events:
                #client socket not yet accepted
                if key.data is None:
                    accept_wrapper(key.fileobj)
                else:
                    #client socket is already accepted
                    service_connection(key, mask)
                    
except socket.error as e:
    print('connection error: {}'.format(e.args()))

