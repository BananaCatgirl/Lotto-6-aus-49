import random

class Ziehung:
    def __init__(self, zahlen, superzahl):
        self.zahlen = zahlen
        self.superzahl = superzahl
        self.jackpot = 1000000

    def ZiehungErstellen(self):
        self.ziehung_zahlen = random.sample(range(1, 50), 6)
        self.ziehung_super = random.randint(1, 9)
        x = self.Vergleich()
        if x == 6:
            return x
        else:
            gewinn = self.jackpot * x
            return gewinn, self.ziehung_super, self.sort()
        
    ausschüttung = {
        6: 0.15,
        5: 0.05,
        4: 0.03,
        3: 0.02,
        2: 6
    }
        
    def Vergleich(self):
        if self.ziehung_super == self.superzahl:
            uebereinstimmungen = sum(1 for zahl in self.zahlen if zahl in self.ziehung_zahlen)
            if uebereinstimmungen > 1:
                return self.ausschüttung.get(uebereinstimmungen, 0)
            else:
                return 0
        else:
            return 0
        
    def sort(self):
        sorted = False
        l = self.ziehung_zahlen
        while not sorted:
            sorted = True
            for i in range(len(l) - 1):
                if l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]
                    sorted = False
        return l
    
i = 1           
def starte_ziehung(list, super):
    global i 
    ziehung = Ziehung(list, super)
    x, sup, num = ziehung.ZiehungErstellen()
    print(f'Ziehung: {i}, Lotto Nummer: {num} Superzahl {sup} \nGewinn: {x}€')
    i += 1

#Bsp.
#starte_ziehung([1,2,3,4,5,6], 5)
#starte_ziehung([1,2,3,4,5,6], 3)
#starte_ziehung([1,2,3,4,5,6], 3)


# Das Programm erwartet das man die Funktion "starte_ziehung" mit den variablen für 
# die Liste mit den 6 nummern und der superzahl startet. Dannach bekommt man den Gewinn wieder.