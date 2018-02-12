from components.conversion import conversion
from components.send import send
from components.receive import receive

dest = '192.168.178.31'
menuopt = input("what do you want to do?\n"
                "1 to encode\n"
                "2 to decode\n")
if menuopt == '1':
    sentence = input("what is your sentence? ")
    morse = (conversion().mto(sentence))
    print(morse)
    send().client(morse, dest)
    receive().client()
if menuopt == '2':
    code = input('what is your code? ')
    conversion().mfrom(code)
