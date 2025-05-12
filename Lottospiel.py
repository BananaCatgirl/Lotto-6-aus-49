# eine Managenment Klasse welche das komplette geschehen des Lotto spieles steuert

#es werden Lottokarten erstellt
# es wird kassiert
# es wird eine ziehung gestartet

from LottoKarte.LottoKarte import LottoKarte
import Ziehung.LottoZiehung
from Kasse.Kasse import Kasse


class Lottospiel:
	def __init__(self):
		self.Lottokarten = []

	def StartLottoKarten(self):
		try:
			weitererStimmzettel = True
			while weitererStimmzettel:
				karte = LottoKarte()
				karte.Setup()
				self.Lottokarten.append( karte )
				if len(karte.GetSpiele()) == 18:
					angabeValid = True
					while not angabeValid:
						angabe = input("wolen sie eine weitere Karte ausfüllen?(ja/nein): ").lower()
						match(angabe):
							case "ja":
								angabeValid = True
								weitererStimmzettel = True
								break
							case "nein":
								angabeValid = True
								weitererStimmzettel = False
								break
							case _:
								angabeValid = False
				else:
					weitererStimmzettel = False
		except:
			print("Fehler beim ausführen der KartenLogic")


	def StartKasse(self):
		try:
			self.Kasse = Kasse(self.Lottokarten)
			#abrechnung = self.Kasse.Abrechnen()
		except:
			print("Fehler beim ausführen der Kasse")


	def StartZiehung(self):
		try:
			pass
		except:
			print("Fehler beim ausführen der Ziehung")


def main():
	while True:
		HauptSpiel = Lottospiel()
		HauptSpiel.StartLottoKarten()
		HauptSpiel.StartKasse()
		HauptSpiel.StartZiehung()
		pass

if __name__ == "main":
	print("\n\nWilkommen zu Lotto 6 aus 49\n\n")
	main()