import socket
from sockdes import SocketDeserializer

SockDes = SocketDeserializer()

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_sock.bind(("127.0.0.1", 8000))
server_sock.listen(5)

with open('index.html', 'rb') as f:
    html_file = f.read()

while True:
    clsock, addr = server_sock.accept()
    print(f"Received request from {addr}")
    a = clsock.recv(1000)
    SockDes.deserialize(a)
    clsock.send('HTTP/1.0 201 OK\n'.encode('utf-8'))
    clsock.send('Content-Type: text/html\n'.encode('utf-8'))
    clsock.send('\n'.encode('utf-8'))
    clsock.send(html_file)
    clsock.close()
