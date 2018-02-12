from components.conversion import conversion
from components.send import send
from components.receive import receive
import threading

devices = {}

while True:

    data, ip = receive().receive()
    print('incoming data.. ' + data)
    if data[0:6] == 'MORSE:':
        #clientsocket.send("Got morse code, sending ack".encode())
        code = data[6:]
        recvsentence = conversion().mfrom(code)
        print('[Received sentence is "' + str(recvsentence) + '"]')
        
        #send(ip).send(recvsentence)
    
    if data[0:5] == 'NAME:':
        print('updateing dictionary')
        print(devices)
        devices.update({data[5:]:ip})
    else:
        print(data)
