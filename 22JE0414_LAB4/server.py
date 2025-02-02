import socket
import os

# Defining server constants
HOST = '127.0.0.1' # Localhost
PORT = 8080 # Server port

def start_server():
    """Start the server to receive files."""
    try:
        # Creating a socket and binding to host and port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1) # Listening for one client at a time
        print(f"Server is listening on {HOST}:{PORT}...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connected to client at {addr}")

            try:
                # Receiving the file name
                file_name = conn.recv(1024).decode()
                if not file_name:
                    print("No file name received. Closing connection.")
                    conn.close()
                    continue

                print(f"Receiving file: {file_name}")
                with open(file_name, 'wb') as f:
                    while True:
                        chunk = conn.recv(1024)
                        # Ending file transfer
                        if chunk == b'EOF': 
                            break
                        f.write(chunk)

                print(f"File {file_name} received successfully.")
                # Acknowledging successful reception
                conn.sendall(b'ACK') 

            # Reporting error during file ftransfer (if any)
            except Exception as e:
                print(f"Error during file transfer: {e}")
            
            # Closing connection
            finally:
                conn.close()
                print("Connection closed.")
    # Reporting server error
    except Exception as e:
        print(f"Server error: {e}")
    # Closing connection 
    finally:
        server_socket.close()

# Establishing client-server connection
start_server()
