#Na podstawie kalkulatora RPN opracuj serwer dostępny dla jednego użytkownika zapewniający
#dostęp przez protokół telnet na wybranym porcie.

import socket
import time 
import operator

operatory = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def obliczzRPN(wyr):
    stos = []
    for znak in wyr:
        if set(znak).issubset(set("0123456789.")):
            stos.append(float(znak))
        elif znak in operatory:
            a = stos.pop()
            b = stos.pop()
            op = operatory[znak]
            stos.append(op(b,a))
    return stos


HOST = '127.0.0.1'
PORT = 2031

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    klient, adres = s.accept()
    while True:
        klient.send(bytes("Wpisz wyrazenie w RPN: ", "utf-8"))
        dane = klient.recv(100)
        wyrazenie =''
        while dane != b'\r\n':
            dekodowane = dane.decode()
            wyrazenie += dekodowane
            temp = klient.recv(100)
            dane = temp
        wynik = obliczzRPN(wyrazenie.split())
        print(wynik)
        klient.send(bytes(str(wynik) + '\n\r', "utf-8"))
