class Kasse:
    def __init__(self, Lottokarten):
        self.Lottokarten = Lottokarten

        while True:
            # Eingabe des Namens usw.
            print("Gebe deinen Vornamen ein")
            self.vorname = input()
            print("Gebe deinen Nachnamen ein")
            self.nachname = input()
            print(f"{self.vorname}, {self.nachname}, stimmen diese Daten? (ja/nein)")
            if input().lower() == "ja":
                break
            else:
                print("Bitte geben Sie die Daten erneut ein.")

        # Adresse und Postleitzahl
        print("Wie lautet Ihre Adresse und Postleitzahl?")
        self.adresse = input("Adresse: ")
        try:
            self.postleitzahl = int(input("Postleitzahl: "))
        except ValueError:
            print("Bitte eine gültige Zahl für die Postleitzahl eingeben.")
            self.postleitzahl = None

        # Email abfragen
        print("Wie lautet Ihre E-Mail-Adresse, damit Sie benachrichtigt werden, wenn die Ziehung erfolgt ist?")
        self.email = input("E-Mail: ")

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
k = Kasse([])