import socket
import os

# Defining server constants
SERVER_HOST = '127.0.0.1' # Server address
SERVER_PORT = 8080 # Server port

def send_file(file_path):
    """Send a file to the server."""

    # Checking if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    try:
        # Creating a socket and connecting to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to the server.")

        # Sending the file name
        file_name = os.path.basename(file_path)
        client_socket.sendall(file_name.encode())

        # Sending the file in chunks
        print(f"Sending file: {file_name}")
        with open(file_path, 'rb') as f:
            while chunk := f.read(1024):
                client_socket.sendall(chunk)

        # Sending EOF marker
        client_socket.sendall(b'EOF')

        # Waiting for acknowledgment
        ack = client_socket.recv(1024).decode()
        if ack == 'ACK':
            print(f"File {file_name} sent successfully.")
        else:
            print("Failed to receive acknowledgment from the server.")
    
    # Reporting error during file ftransfer (if any)
    except Exception as e:
        print(f"Error during file transfer: {e}")
    # Closing connection
    finally:
        client_socket.close()

# Getting the file path from the user and sending it to the server
file_path = input("Enter the file path to upload: ")
send_file(file_path)

