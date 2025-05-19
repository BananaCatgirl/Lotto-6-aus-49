import zahlenAuswahl
class Spiel:
	def __init__(self):
		self.zahlenAngekreuzt = [] # 6 zahlen die von spieler angekreuzt werden

	def GetAngekreuzteZahlen(self):
		return self.zahlen
	
	def Ankreuzen(self):
		ankreuzenGültig = False
		while not ankreuzenGültig:
			try:
				print("\n1.manuell\n2.zufall\n3.Sternzeichen\n")
				auswahl = int(input("wie wollen sie die zahlen festlegen?(1/2/3)"))
				if auswahl == 1:
					zahlenAuswahl.manuellWählen
				else:
					ankreuzenGültig = False
			except:
				print("we fucked up beim zahlen auswählen")
		zahlen = []
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