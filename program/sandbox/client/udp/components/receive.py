from socket import *
class receive:
    def __init__(self):
        pass
    def receive(self):
        host = ""
        port = 13333
        buf = 1024
        address = (host, port)
        UDPsock = socket(AF_INET, SOCK_DGRAM)

        UDPsock.bind(address)
        print("receiving")
        (data, addr) = UDPsock.recvfrom(buf)
        print('received')
        UDPsock.close()
        print(data)
        return data, addr

