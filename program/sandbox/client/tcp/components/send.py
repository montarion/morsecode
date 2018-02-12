from socket import *
class send:
    def __init__(self):
        pass
    def client(self, morse):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(("192.168.178.31", 13333))
        morse = "MORSE: " + morse
        s.send(morse.encode())
        print(s.recv(2048).decode())
