
from socket import *
from threading import *

# constants
HOST='localhost'
PORT=3001
NO_OF_CONNECTIONS=10



#function to handle all clients 
def handle_client(client , address):
    while True:
        raw_response = client.recv(1024)
        response = raw_response.decode()
        print('response from ' , address)
        print('response ' , response)
        text = input("Enter text (enter to exit) ")
        client.send(bytes(text.encode()))
    client.close()
server_socket = socket()
server_socket.bind((HOST , PORT))
# max connection
server_socket.listen(10)
print('server started PORT : ',PORT)
while True:
    client , address = server_socket.accept()
    thread = Thread(target=handle_client,args=(client ,address))
    thread.start()
server_socket.close()
