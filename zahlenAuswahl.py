import random
from datetime import datetime
def manuellWählen():
	pass
def RandomWählen():
	random.seed()	
	zahlen = []
	for i in range(6):
		zufallsZahl = random.randint(1,49)
		while zahlen.count(zufallsZahl) > 0:
			zufallsZahl = random.randint(1,49)

		zahlen.append(zufallsZahl)
	superzahl = random.randint(1,9)
	return zufallsZahl, superzahl


def SternzeichenWählen():
	while True:
		abfrage_sternzeichen = input("Bitte geben Sie Ihr Sternzeichen ein: ").lower()
		if abfrage_sternzeichen == "widder":
			sternzeichen = 1
			break
		elif abfrage_sternzeichen == "stier":
			sternzeichen = 2
			break
		elif abfrage_sternzeichen == "zwilling":
			sternzeichen = 3
			break
		elif abfrage_sternzeichen == "krebs":
			sternzeichen = 4
			break
		elif abfrage_sternzeichen == "löwe":
			sternzeichen = 5
			break
		elif abfrage_sternzeichen == "jungfrau":
			sternzeichen = 6
			break
		elif abfrage_sternzeichen == "waage":
			sternzeichen = 7
			break
		elif abfrage_sternzeichen == "skorpion":
			sternzeichen = 8
			break
		elif abfrage_sternzeichen == "schütze":
			sternzeichen = 9
			break
		elif abfrage_sternzeichen == "steinbock":
			sternzeichen = 10
			break
		elif abfrage_sternzeichen == "wassermann":
			sternzeichen = 11
			break
		elif abfrage_sternzeichen == "fische":
			sternzeichen = 12
			break
		else:
			print("Ungültiges Sternzeichen, nutze folgende Eingaben: \nWidder, Stier, Zwillinge, Krebs, Löwe, Jungfrau, Waage, Skorpion, Schütze, Steinbock, Wassermann, Fische")
			continue

	heute = int(datetime.now().strftime("%d%m%Y%H%M"))
	zahlen = heute / sternzeichen
	zahlen_str = str(int(zahlen))
	auswahl = [int(zahlen_str[i:i+2]) for i in range(0, len(zahlen_str), 2)][:6]

	for i in range(len(auswahl)):
		while auswahl.count(auswahl[i]) > 1 or auswahl[i] > 49 or auswahl[i] < 1:
			auswahl[i] += 1
			if auswahl[i] > 49:
				auswahl[i] = 1

	superzahl = zahlen_str[-1]
	if superzahl == "0":
		superzahl = 1
	return auswahl, superzahl
