import socket

HOST = '127.0.0.1'
PORT = 65432

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
