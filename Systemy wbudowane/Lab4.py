#Opracuj klasę (z określeniem ale bez implementacji metod) opisującą dowolne urządzenie
#techniczne. Przedstaw szkielet w j. Python.

class Drukarka:
    licznik = 0

    def __init__(self, nazwa, iloscStronDoWydruku):
        Drukarka.licznik += 1
        self.nazwa = nazwa
        self.iloscStron = iloscStronDoWydruku
        
    def pokazNazwe(self):
        print(f'Jestem drukarka {self.nazwa}')

    def wlacz(self):
        print('Jestem wlaczana')

    def wylacz(self):
        print('Jestem wylaczana')

    def drukuj(self):
        print ('Drukuje')

    def pokazIloscTusz(self):
        print ('Pokazuje ilosc tuszu')

    def pokazIloscStron(self):
        print ('Wydrukuje {self.iloscStron} stron')

    @staticmethod
    def ileDrukarek():
        return Drukarka.licznik
        
    






