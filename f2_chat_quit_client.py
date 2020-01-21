import socket

chat_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

chat_socket.connect((address, port))
while True:
    print('WAITING FOR SERVER...')
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    if data == b'quit\n':
        break
    print('SERVER WROTE: ' + data.decode())
    data = input('INPUT CLIENT: ').encode()
    chat_socket.sendall(data + b'\n')
    if data == b'quit':
        break

chat_socket.close()
