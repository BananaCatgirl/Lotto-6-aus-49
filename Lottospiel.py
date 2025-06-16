# eine Managenment Klasse welche das komplette geschehen des Lotto spieles steuert

#es werden Lottokarten erstellt
# es wird kassiert
# es wird eine ziehung gestartet

from LottoKarte import LottoKarte
import LottoZiehung as Ziehung
from Kasse import Kasse
import Spiel


class Lottospiel:
	def __init__(self):
		self.Lottokarten = []

	def StartLottoKarten(self):
		try:
			weitererStimmzettel = True
			while weitererStimmzettel:
				weitererStimmzettel = False
				self.karte = LottoKarte()
				self.karte.Setup() #setup der Lottokarte wie z.b. spiele menge 1-18, tage an denen gelost wird
				self.Lottokarten.append( self.karte )
				if len(self.karte.GetSpiele()) == 18:
					angabeValid = True
					while not angabeValid:
						angabe = input("wollen sie eine weitere Karte ausfüllen?(ja/nein): ").lower()
						match(angabe):
							case "ja":
								angabeValid = True
								weitererStimmzettel = True
								
							case "nein":
								angabeValid = True
								weitererStimmzettel = False
								
							case _:
								print("entschuldigung, aber die eingabe war nicht gültig")
								angabeValid = False
				else:
					weitererStimmzettel = False
		except:
			print("Fehler beim ausführen der KartenLogic")


	def StartKasse(self):
		self.Lottokarten = LottoKarte.GetMengeSpiele()
		try:	
			self.Kasse = Kasse(self.Lottokarten)
			abrechnung = self.Kasse.Abrechnen()
		except:
			print("Fehler beim ausführen der Kasse")


	def StartZiehung(self):
		x = self.karte.GetSpiele()
		x[0].Getzahlenangekreuzt()
		try:
			#Ziehung.starte_ziehung(, )
			pass
		except:
			print("Fehler beim ausführen der Ziehung")


def main():
	runProgramm = True
	while runProgramm:
		runProgramm = False
		print("\n\n\n\n\nWilkommen zu Lotto 6 aus 49\n\n")
		HauptSpiel = Lottospiel()
		HauptSpiel.StartLottoKarten()
		HauptSpiel.StartKasse()
		HauptSpiel.StartZiehung()

if __name__ == "__main__":
	main()