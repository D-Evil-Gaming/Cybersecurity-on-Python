import socket
import threading
from queue import Queue

target="192.168.15.10"
q=Queue()
open=[]

def portscanner(port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        return True
    except:
        return False
    
def fill_ports(port_lists):
    for port in port_lists:
        q.put(port)

def workers():
    while not q.empty():
        d=q.get()
        if portscanner(d):
            print(f"{d} is open port")
            open.append(d)

port_lists=range(1,1024)
fill_ports(port_lists)

thre=[]
for i in range(100):
    thread = threading.Thread(target=workers)
    thre.append(thread)

for i in thre:
    i.start()

for i in thre:
    i.join()

print(f"Open ports {open}")