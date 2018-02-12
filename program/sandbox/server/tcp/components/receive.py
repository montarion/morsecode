from socket import *
from time import sleep
class receive:
    def __init__(self):
        self.ss = socket(AF_INET, SOCK_STREAM)
        self.ss.bind(('', 13333))
        self.ss.listen(5)

    def receive(self):

            print('ready to connect')
            # accept connections from outside
            (clientsocket, address) = self.ss.accept()
            data = clientsocket.recv(2048).decode()
            ip = address[0]

            return data, ip
