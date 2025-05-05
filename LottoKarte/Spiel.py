

class Spiel:
	def __init__(self,z1,z2,z3,z4,z5,z6):
		self.zahlen = [z1,z2,z3,z4,z5,z6] # 6 zahlen die von spieler angekreuzt werden

	def GetZahlen(self):
		return self.zahlen