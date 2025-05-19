class Kasse:
	def	__init__(self,Lottokarten):
		self.Lottokarten = Lottokarten

		while True:
			#Eingabe des names usw
			print("Gebe deinen Vornamen ein")
			self.vorname = input()
			print("Gebe deinen Nachnamen ein")
			self.nachname = input()
			print("self.vorname, self.nachname, stimmen diese Daten?")
			

		#Adresse und Postleitzahl
		print("Wie lautet Ihre Adresse und Postleitzahl?")
        adresse = input("Adresse: ")
        try:
		postleitzahl = int(input("Postleitzahl: "))
        except ValueError:
            print("Bitte eine gültige Zahl für die Postleitzahl eingeben.")
            postleitzahl = None

        # Email abfragen
        print("Wie lautet Ihre E-Mail-Adresse, damit Sie benachrichtigt werden, wenn die Ziehung erfolgt ist?")
        email = input("E-Mail: ")

        # Bestätigung der Eingaben
        
		print("\nIhre Eingaben:")
        print("Adresse:", self.adresse)
        print("Postleitzahl:", self.postleitzahl)
        print("E-Mail:", self.email)
        print("Stimmen diese Daten? (ja/nein)")
        self.bestaetigung = input().lower()
        if self.bestaetigung != "ja":
            print("Bitte starten Sie die Eingabe erneut.")
        else:
            print("Vielen Dank! Ihre Daten wurden gespeichert.")

# Objekt erzeugen
k = Kasse()