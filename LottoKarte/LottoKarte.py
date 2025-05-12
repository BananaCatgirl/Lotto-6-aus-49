class LottoKarte:
	def __init__(self):
		self.spiele = []
		self.mittwochsZiehung = False
		self.SamstagsZiehung = False

	def Setup(self):# wieviele spiele aus 18max? welche losungs tage?
		# spiele menge abfrage
		gewünschteSpieleMenge = 0
		
		Fehler = False
		while not Fehler:
			try:
				gewünschteSpieleMenge = int(input("wieviel spiele wollen sie spielen?(1-18): "))
				if(gewünschteSpieleMenge > 18 ):
					print("angabe wa größer 18. zahl wid auf 18 gecapt")
				elif(gewünschteSpieleMenge < 1):
					print("zahl führ spiele menge zu klein. Setze wert auf 1")
			except:
				print("sorry das ist keine gültige angabe.\n")
				Fehler = True

		#Abfrage für ziehung tage
		ungültig = False
		tagesAbfrage = -1
		while not ungültig:
			try:
				ungültig = False
				print("\n\n1.Mittwoch\n2.Samstag\n3.Beide Tage")
				tagesAbfrage = int(input("an welchen Tagen wollen sie spielen?(1/2/3):"))
				if tagesAbfrage != 1 or tagesAbfrage != 2 or tagesAbfrage != 3:
					print("ungültige angabe! bitte wiederholen!")
					ungültig = True
			except:
				print("angabe war nicht gültig.")
				ungültig = True

		match tagesAbfrage:
			case 1:
				pass
			case 2:
				pass
			case 3:
				pass

		

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
	