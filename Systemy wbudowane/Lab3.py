#Opracuj program, korzystający z wyrażeń regularnych zmień przykładowy nagłówek wiadomości
#From: author@example.com
#User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
#MIME-Version: 1.0
#To: editor@example.com
#w słownik.


import re

slownik={}

podzialWersow=[]

tekst = """From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com"""

wersy = re.split('\n', tekst)

klucz=':\s'

for i in range(len(wersy)):
    podzialWersow.append(re.split(klucz, wersy[i]))
    slownik[podzialWersow[i][0]]=podzialWersow[i][1]
    



        
    
