from socket import *
class send:
    def __init__(self):
        pass
    def client(self, morse, dest):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((dest, 13333))

        s.send(("MORSE:" + morse).encode())
        print(s.recv(2048).decode())
