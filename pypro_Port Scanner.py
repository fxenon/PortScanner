# **********************************************************************************************************************
# ----------------------------------------------------Port Scanner------------------------------------------------------
# **********************************************************************************************************************

import socket
import threading
from queue import Queue

target = "127.0.0.1"
queue = Queue()
open_ports = []


def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queue(list_of_ports):
    for port in list_of_ports:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print(f'port {port} is open')
            open_ports.append(port)


port_list = range(1, 1025)
fill_queue(port_list)

thread_list = []

for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("open ports are: ", open_ports)




