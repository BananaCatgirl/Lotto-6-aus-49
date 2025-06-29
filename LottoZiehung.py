import random, time

class Ziehung:
    def __init__(self, zahlen, superzahl):
        self.zahlen = zahlen
        self.superzahl = superzahl
        self.jackpot = 1000000

    def ZiehungErstellen(self):
        self.ziehung_zahlen = random.sample(range(1, 50), 6)
        self.ziehung_super = random.randint(1, 9)
        anteil = self.Vergleich()
        if anteil == 6:
            gewinn = 6
        else:
            gewinn = self.jackpot * anteil
        return round(gewinn, 2), self.ziehung_super, self.sort()
        
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
    gewinn, sup, num = Ziehung(list, super).ZiehungErstellen()
    
    print(f'Ziehung {i}:')
    for y in range(0, len(num), 3):
        print(num[y],"|", num[y+1],"|", num[y+2])
    print(f'Superzahl: {sup}\nGewinn: {gewinn}€\n')
    i += 1
    return gewinn

#Bsp.
#starte_ziehung([1,2,3,4,5,6], 5)
#starte_ziehung([1,2,3,4,5,6], 3)
#starte_ziehung([1,2,3,4,5,6], 3)


# Das Programm erwartet das man die Funktion "starte_ziehung" mit den variablen für
# die Liste mit den 6 nummern und der superzahl startet. Danach bekommt man den Gewinn wieder.