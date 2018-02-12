from socket import *
class send:
    def __init__(self, dest, msg):
        self.msg = msg
        self.dest = dest
    def send(self):
        msg = "hey client!"     #will be msg
        host = "192.168.178.31" #will be dest
        port = 13333
        buf = 1024
        addr = ((host, port))
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        UDPSock.bind((addr))
        UDPSock.sendto(bytes(msg, "UTF-8"), addr)
        UDPSock.close()
        print('sent ', msg, 'to ', host)


