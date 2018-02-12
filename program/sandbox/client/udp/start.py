from components.receive import receive
from components.send import send
msg = 'NAME:testdev1'
send(msg).send()
print('ready to recieve')
data, addr = receive().receive()
print(data)
