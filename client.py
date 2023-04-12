import socket
import threading
import logging
#import time
import sys

logging.basicConfig(filename='client.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

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

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(nickname.encode())
            else:
                message = qwerty_positional_decode(message)
                print(message)
                logging.info(f'Message received: {message}')
        except Exception as e:
            if e.args[0] == 10053:
                logging.info("The connection was closed correctly")
                client.close()
            else:
                logging.error("Exception occurred", exc_info=True)
            break
        except:
            print("Error!")
            logging.warning('message couldn´t be received')
            break

def write():
    while True:
        inpt = input()
        if  inpt == '':
            client.close()
            logging.info("program finished")
            break
        message = f'{nickname}: {inpt}'
        logging.info(f"Message send: {message}")
        message = qwerty_positional_encode(message)
        logging.info(f"Message encoded: {message}")
        client.send(message.encode())

command = sys.argv
if len(command) == 2:
    nickname = str(sys.argv[1])
elif len(command) == 1:
    nickname = input("Choose a nickname: ")
else:
    logging.error("Using a bad command")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    client.connect(('127.0.0.1',50000))
    receive_thread = threading.Thread(target = receive)
    receive_thread.start()

    write_thread = threading.Thread(target = write)
    write_thread.start()

except Exception as e:
    logging.error("Couldn't connect with the chat!")