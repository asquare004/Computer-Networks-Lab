import socket
import threading
import sys

# Details of server host and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8081

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            print(msg)
        except:
            print("Disconnected from server.")
            client_socket.close()
            break
        
# This function establishes connection between server and client
def start_client():
    if len(sys.argv) < 2:
        print("Usage: python client.py <Your_Name>")
        return

    name = sys.argv[1]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_HOST, SERVER_PORT))
    client.send(name.encode())

    threading.Thread(target=receive_messages, args=(client,)).start()

    while True:
        msg = input()
        if msg.lower() == "exit":
            client.send(msg.encode())
            break
        client.send(msg.encode())

    client.close()

start_client() 
