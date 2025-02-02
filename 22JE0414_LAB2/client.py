# UDP client code

import socket 

# Creating a client socket and binding it to an IP address and a port number
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8081)

# Sending a message to server 
client_socket.sendto('This is a text message'.encode(), server_address)

# Receiving a message from server
data, _ = client_socket.recvfrom(1024)
print(f'Received from server : {data.decode()}')

# Closing the client socket
client_socket.close()