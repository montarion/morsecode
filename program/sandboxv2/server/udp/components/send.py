from socket import *
class send:
    def __init__(self, dest, msg):
        self.msg = msg
        self.dest = dest
    def send(self):
        msg = "MORSE:...._._-.--_"     #will be msg
        host = "192.168.178.31" #will be dest
        port = 13334
        buf = 1024
        addr = (('<broadcast>', port))
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDPSock.bind((addr))
        UDPSock.sendto(bytes(msg, "UTF-8"), addr)
        UDPSock.close()
        print('sent ', msg, 'to ', host)


