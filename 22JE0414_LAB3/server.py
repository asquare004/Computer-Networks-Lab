import socket
import threading
import datetime

# Host and port 
HOST = '127.0.0.1'
PORT = 8081
clients = {} # Dictionary to store all client sockets and their corresponding names

# Function to log all messages into server_logs.txt
def log_message(message): 
    with open("server_log.txt", "a") as log_file: #Append the message in 
        log_file.write(f"{message}\n")

# Function to broadcast messages to all clients in the server
def broadcast(message, sender = None):
    log_message(message)
    for client, name in clients.items():
        if client != sender:
            try:
                client.send(message.encode())
            except:
                client.close()
                del clients[client]

# Function for chatting feature
def handle_client(client_socket):
    try:
        name = client_socket.recv(1024).decode()
        clients[client_socket] = name
        print(f"{name} has joined the chat.")
        broadcast(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {name} joined the chat.", client_socket)

        while True:
            msg = client_socket.recv(1024).decode()
            if msg.lower() == "exit":
                break
            elif msg.lower() == "list":
                client_list = "Connected clients: " + ", ".join(clients.values())
                client_socket.send(client_list.encode())
            elif msg.startswith("@"):
                recipient, _, message = msg.partition(" ")[2:].partition(" ")
                for sock, uname in clients.items():
                    if uname == recipient:
                        sock.send(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {name} (Private): {message}".encode())
                        break
            else:
                timestamp = datetime.datetime.now().strftime('%H:%M:%S')
                broadcast(f"[{timestamp}] {name}: {msg}", client_socket)

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        print(f"{clients[client_socket]} has left the chat.")
        broadcast(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {clients[client_socket]} left the chat.")
        del clients[client_socket]
        client_socket.close()

# This function binds a server socket to its corresponding socket address and port number
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Server started on port", PORT)

    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

start_server()

