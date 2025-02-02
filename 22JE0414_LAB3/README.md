# Multi-Client Server Using Threads

In the third lab session, I implemented a multi-client chat system using Pyhton sockets and threads. It allows multiple clients to connect, communicate via broadcast messages, and disconnect gracefully. The server handles each client in a separate thread and logs all messages with timestamps.

## How to Use ?

1. First run server.py

2. Run client.py and use "python client.py <your-name>" to create a new user (client) with name <your-name>

3. Repeat step 3 for multiple users.

4. Each client can chat with all other clients via their corresponding interface.

5. You can send "list" in your interface to get the list of clients currently active.

6. You can exit from the chat by sending "exit".

7. All messages are stored in server_log.txt