from components.conversion import conversion
from components.send import send
from components.receive import receive
import threading


while True:

    data, ip = receive().receive()

    if data[0:6] == 'MORSE:':
        #clientsocket.send("Got morse code, sending ack".encode())
        code = data[7:]
        recvsentence = conversion().mfrom(code)
        print('[Received sentence is "' + recvsentence + '"]')
        send(ip).send(code)
