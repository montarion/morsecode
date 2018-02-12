from socket import *
from time import sleep
class send:
    def __init__(self, ip):
        self.ss = socket(AF_INET, SOCK_STREAM)
        self.ss.connect(((ip), 13334))


    def send(self, code):
        print('ready to send')
        self.ss.send(code.encode())
        print('sent')
        self.ss.close()
