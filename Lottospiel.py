# eine Managenment Klasse welche das komplette geschehen des Lotto spieles steuert

#es werden Lottokarten erstellt
# es wird kassiert
# es wird eine ziehung gestartet

from LottoKarte.LottoKarte import LottoKarte
from Ziehung.Ziehung import Ziehung
from Kasse.Kasse import Kasse


class Lottospiel:
	def __init__(self):
		self.Lottokarten = []
		self.Kasse = Kasse()
		self.Ziehung = Ziehung()

	def StartLottoKarten(self):
		try:
			pass
		except:
			print("Fehler beim ausführen der KartenLogic")


	def StartKasse(self):
		try:
			pass
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