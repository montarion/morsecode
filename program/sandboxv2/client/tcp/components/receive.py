from socket import *
from time import sleep
class receive:
    def __init__(self):
        self.ss = socket(AF_INET, SOCK_STREAM)
        self.ss.bind(('', 13334))
        self.ss.listen(5)

    def client(self):
        clientsocket = self.ss.accept()
        data = clientsocket.recv(2048).decode()
        return data
