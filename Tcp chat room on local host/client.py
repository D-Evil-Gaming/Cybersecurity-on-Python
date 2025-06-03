import socket
import threading

nickname = input("Enter a Nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55556))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "Nick":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred.")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('ascii'))

thread = threading.Thread(target=receive)
thread.start()

wri = threading.Thread(target=write)
wri.start()
