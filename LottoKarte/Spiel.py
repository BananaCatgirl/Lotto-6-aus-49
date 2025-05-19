class Spiel:
	def __init__(self):
		self.zahlenAngekreuzt = [] # 6 zahlen die von spieler angekreuzt werden

	def GetAngekreuzteZahlen(self):
		return self.zahlen
	
	def Ankreuzen(self,z1,z2,z3,z4,z5,z6):

		zahlen = [z1,z2,z3,z4,z5,z6]
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