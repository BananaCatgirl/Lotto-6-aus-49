import zahlenAuswahl
class Spiel:
	def __init__(self):
		self.zahlenAngekreuzt = [] # 6 zahlen die von spieler angekreuzt werden
		self.superzahl = 0

	def GetAngekreuzteZahlen(self) -> list[int]:
		return self.zahlenAngekreuzt
	
	def GetSuperzahl(self) -> int:
		return self.superzahl

	def Ankreuzen(self):
		ankreuzenGültig = False
		while not ankreuzenGültig:
			try:
				print("\n1.manuell\n2.zufall\n3.Sternzeichen\n")
				auswahl = int(input("wie wollen sie die zahlen festlegen?(1/2/3)"))
				if auswahl == 1:
					zahlen, superzahl = zahlenAuswahl.manuellWählen()
					ankreuzenGültig = True
				elif auswahl == 2:
					zahlen, superzahl = zahlenAuswahl.RandomWählen()
					ankreuzenGültig = True
				elif auswahl == 3:
					zahlen, superzahl = zahlenAuswahl.SternzeichenWählen()
					ankreuzenGültig = True
				else:
					ankreuzenGültig = False
			except:
				print("we fucked up beim zahlen auswählen")

		print("danke für deine ausgewählten zahlen")
		zahlenDieExistieren = []
		for zahl in zahlen:
			if zahl in zahlenDieExistieren:
				print("\n eine zahl kann nicht doppelt vorkommen.")
				return False
			else:
				zahlenDieExistieren.append(zahl)

		self.zahlenAngekreuzt = []
		if len(zahlenDieExistieren) != 6:
			print("die menge an angekreuzten zahlen ist nicht 6. Das sollte so nicht sein.")
		else:
			self.zahlenAngekreuzt = zahlenDieExistieren
			self.superzahl = superzahl
