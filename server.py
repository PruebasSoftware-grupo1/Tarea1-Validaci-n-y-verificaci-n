import socket
import threading

host = '127.0.0.1'
port = 50000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicks = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nick = nicks[index]
            nick.remove(nick)
            broadcast(f"{nick} has been BANNED.".encode())
            break

def receive():
    while (True):
        client, address = server.accept()
        print(f"Connect with address {str(address)}")
        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        nicks.append(nickname)
        clients.append(client)
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} join the chat.".encode())
        client.send("You are connected to the chat".encode())

        thread = threading.Thread(target = handle, args = (client,))
        thread.start()
print("Server On...")
receive()