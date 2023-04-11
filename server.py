import socket
import threading
import logging

logging.basicConfig(filename='server.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')
host = '127.0.0.1'
port = 50000


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicks = []

def qwerty_positional_encode(message):
    qwerty_map = {
        'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
        'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
        'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
        'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
        'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n',
        'z': 'm', ' ': ' '
    }
    encoded_message = ''
    for i, char in enumerate(message):
        if char in qwerty_map:
            shift = i + 1
            qwerty_pos = list(qwerty_map.keys()).index(char)
            shifted_pos = (qwerty_pos + shift) % len(qwerty_map)
            encoded_message += qwerty_map[list(qwerty_map.keys())[shifted_pos]]
        else:
            encoded_message += char
    return encoded_message

def qwerty_positional_decode(encoded_message):
    qwerty_map = {
        'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e',
        'y': 'f', 'u': 'g', 'i': 'h', 'o': 'i', 'p': 'j',
        'a': 'k', 's': 'l', 'd': 'm', 'f': 'n', 'g': 'o',
        'h': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'z': 't',
        'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y',
        'm': 'z', ' ': ' '
    }
    decoded_message = ''
    for i, char in enumerate(encoded_message):
        if char in qwerty_map:
            shift = i + 1
            qwerty_pos = list(qwerty_map.keys()).index(char)
            shifted_pos = (qwerty_pos - shift) % len(qwerty_map)
            decoded_message += qwerty_map[list(qwerty_map.keys())[shifted_pos]]
        else:
            decoded_message += char
    return decoded_message

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        if clients == []:
            logging.info("Server down")
            break
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nick = nicks[index]
            nicks.remove(nick)
            notification = f"{nick} is gonne."
            broadcast(notification.encode())
            if clients == []:
                logging.info("Server down")
                server.close()
            break

def receive():
    while (True):
        try:
            client, address = server.accept()
            print(f"Connect with address {str(address)}")
            nick_request = 'NICK'
            client.send(nick_request.encode())
            nickname = client.recv(1024).decode()
            nicks.append(nickname)
            clients.append(client)
            print(f"Nickname of the client is {nickname}")

            notification = f"{nickname} join the chat."
            broadcast(notification.encode())

            thread = threading.Thread(target = handle, args = (client,))
            thread.start()
        except Exception as e:
            if e.args[0] == 10038:
                logging.info("Server is closed")
                break
            else:
                logging.info("Error!")


print("Server On...")
receive()