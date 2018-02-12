from components.conversion import conversion
from components.send import send


menuopt = input("what do you want to do?\n"
                "1 to encode\n"
                "2 to decode\n")
if menuopt == '1':
    sentence = input("what is your sentence? ")
    morse = (conversion().mto(sentence))
    send().client(morse)
if menuopt == '2':
    code = input('what is your code? ')
    conversion().mfrom(code)
