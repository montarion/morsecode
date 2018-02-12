from socket import *
from time import sleep
class send:
    def __init__(self, msg):
        self.msg = msg
    def send(self):

        host = "192.168.178.31" #hardcoded serverip
        port = 13333
        buf = 1024
        addr = ((host, port))
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sleep(1)
        UDPSock.sendto(bytes(self.msg, "UTF-8"), addr)
        UDPSock.close()
