# UDP server code

import socket

# Function to convert first five characters of decoded string to corresponding binary code
def string_to_binary(data):
    binary_string = ''.join(format(ord(char), '08b') for char in data[:5])
    return binary_string

# Creating a server socket and binding it to an IP address and a port number
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8081))
print('Listening on port 8081')

# Waiting for data from client 
while True:
    data, addr = server_socket.recvfrom(1024)
    decoded_data = data.decode()
    # Received data from client and decoded it successfully
    print('Acknowledged ', decoded_data)
    # Converting first five characters of decoded client data to binary representation
    converted_data = string_to_binary(decoded_data)
    # Encoding the converted data and send it back to client
    server_socket.sendto(converted_data.encode(), addr)