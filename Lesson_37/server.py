import socket
from threading import Thread
SERVER_HOST = 'localhost' # '0.0.0.0', '127.0.0.1'
SERVER_PORT = 5678
client_connections = set()
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # try experiments !
sock.bind((SERVER_HOST, SERVER_PORT))
sock.listen(5)
print(f'Server ready on {SERVER_HOST}:{SERVER_PORT}')
def listen_for_message(connection):
   while True:
        try:
            message = connection.recv(1024).decode()
        except Exception as ex:
            print(f'Exception: {ex}')
            # continue
        else:
            for conn in client_connections:
                conn.send(message.encode())  # change after (send without me)
while True:
    connection, client_address = sock.accept()
    print(f'connected from client address: {client_address}')
    client_connections.add(connection)
    task = Thread(target=listen_for_message, args=(connection,), daemon=True)
    task.start()

