import socket
import selectors
import types

HOST = '127.0.0.1'
PORT = 65432
'''
#echo client example
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        echo = ''
        while True:
            echo = input()
            if echo == 'bye': break
            echo = bytes(echo, 'utf-8')
            sock.sendall(echo)
            data = sock.recv(1024)
            print(data.decode())
except socket.error as e:
    print('connection error: {}'.format(e.args()))
'''
messages = [b'Message 1 from client.', b'Message 2 from client']

def start_connections(host, port, num_conns):

    global selector
    server_addr = (host, port)
    for i in range(0, num_conns):
        conn_id = i + 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(conn_id=conn_id,
                                     msg_total=sum(len(m) for m in messages)+1,
                                     recv_total=0,
                                     messages=list(messages),
                                     outb=b'')
        selector.register(sock, events, data=data)

def service_connections(key, mask):

    global selector
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        rx = sock.recv(1024)
        if rx:
            data.recv_total += len(rx)
        if not rx or data.recv_total == data.msg_total:
            print(rx)
            print(data.recv_total)
            print(data.msg_total)
            selector.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

try:
    selector = selectors.DefaultSelector()
    start_connections(HOST, PORT, 1)
    while True:
        events = selector.select(timeout=1)
        if events:
            for key, mask in events:
                service_connections(key, mask)
        if not selector.get_map():
            break

except Exception as e:
    print('connection in progress: {}'.format(e.args()))
    selector.close()
