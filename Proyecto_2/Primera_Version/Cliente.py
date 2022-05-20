import socket
import time

HOST = "127.0.0.1" 
PORT = 8
HEADER = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

    strData = str(input())

    data_len = str(len(strData))

    data = f"{data_len:<{HEADER}}{strData}".encode('utf-8')
    #print(data)
    s.send(data)
    time.sleep(1)
    backH = s.recv(1024)
    print(backH)
