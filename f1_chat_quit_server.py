import socket

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 6789))
listen_socket.listen()

chat_socket, addr = listen_socket.accept()
while True:
    data = input('INPUT SERVER: ').encode()
    chat_socket.sendall(data + b'\n')
    if data == b'quit':
        break
    print('WAITING FOR CLIENT...')
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    if data == b'quit\n':
        break
    print('CLIENT WROTE: ' + data.decode())

chat_socket.close()
listen_socket.close()
