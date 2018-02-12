from components.send import send
from components.receive import receive
from time import sleep


data, addr = receive().receive()

print(data)
dest = addr[0]

msg = "hey sweetie"
print('sending to ', dest)
sleep(2)
send(dest, msg).send()

