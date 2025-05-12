class LottoKarte:
	def __init__(self):
		self.spiele = []
		self.mittwochsZiehung = False
		self.SamstagsZiehung = False

	def Setup(self):# wieviele spiele aus 18max? welche losungs tage?
		pass

	def GetSpiele(self) -> int:
		return len(self.spiele)
	
	def GetZiehungsTage(self):
		return (self.mittwochsZiehung,self.SamstagsZiehung)
	
	def GetZiehungsTagMittwoch(self)->bool:
		return self.mittwochsZiehung
	
	def GetZiehungsTagSamstag(self)->bool:
		return self.SamstagsZiehung
	
	