import socket

my_socket = socket.socket()
my_socket.bind(('127.0.0.1', 12345))
my_socket.listen()

new_socket, addr = my_socket.accept()
print('Connected to: ' + str(addr))
print(new_socket.recv(1024))

new_socket.close()
my_socket.close()
