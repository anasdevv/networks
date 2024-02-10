from socket import *

HOST='localhost'
PORT=3001
client_socket = socket()

client_socket.connect(('localhost', 3001))
message = input(f"Enter msg client 1, enter n to end conversation ")
while message.lower().strip() != 'n':
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f'Received from server: ' + data)
    message = input(f"  Enter msg client 1, enter n to end conversation ")
client_socket.close()