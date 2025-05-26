import Spiel as Spiel

class LottoKarte:
	def __init__(self):
		self.spiele = []
		self.mittwochsZiehung = False
		self.SamstagsZiehung = False

	def Setup(self):# wieviele spiele aus 18max? welche losungs tage?
		# spiele menge abfrage
		gewünschteSpieleMenge = 0
		
		breakLoop = False
		while not breakLoop:
			try:
				gewünschteSpieleMenge = int(input("wieviel spiele wollen sie spielen?(1-18): "))
				if(gewünschteSpieleMenge > 18 ):
					print("angabe war größer 18. zahl wid auf 18 gecapt.")
				elif(gewünschteSpieleMenge < 1):
					print("zahl führ spiele menge zu klein. Setze wert auf 1")
				breakLoop = True
				print(f"sie wollen also {gewünschteSpieleMenge} spielen, cool!")
			except:
				print("sorry das ist keine gültige angabe.\n")
				breakLoop = False

		#Abfrage für ziehung tage
		ungültig = True
		tagesAbfrage = -1
		while ungültig:
			try:
				ungültig = True
				print("\n\n1.Mittwoch\n2.Samstag\n3.Beide Tage")
				tagesAbfrage = int(input("an welchen Tagen wollen sie spielen?(1/2/3):"))
				if tagesAbfrage == 1 or tagesAbfrage == 2 or tagesAbfrage == 3:
					print(f"ah okay also wollen sie {tagesAbfrage}")
					ungültig = False
				else:
					print("angabe ungültig.")
					ungültig = True
			except:
				print("angabe für ziehungstage ist abgestürzt.")
				ungültig = True

		match (tagesAbfrage):#an welchen tagen sol gespielt werden
			case 1:#Mittwoch
				self.mittwochsZiehung = True
				print("mittwochs ziehung gesetzt")
			case 2:#Samstag
				self.SamstagsZiehung = True
				print("samstags ziehung gesetzt")
			case 3:#Mittwoch und Samstag
				self.mittwochsZiehung = True
				self.SamstagsZiehung = True
				print("mittwochs und samstags ziehung gesetzt")

		for i in range(gewünschteSpieleMenge):
			try:
				spiel = Spiel.Spiel()
				print(f"\n\n\n Spiel Nummer {i+1}")
				spiel.Ankreuzen()
			except:
				print("we encountered an error while setting a spiel auf einer lottokarte.")

		

	def GetSpiele(self):
		return self.spiele
	
	def GetMengeSpiele(self):
		return len(self.spiele)

	def GetZiehungsTage(self):
		return (self.mittwochsZiehung,self.SamstagsZiehung)
	
	def GetZiehungsTagMittwoch(self)->bool:
		return self.mittwochsZiehung
	
	def GetZiehungsTagSamstag(self)->bool:
		return self.SamstagsZiehung
	