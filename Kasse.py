import LottoKarte as Karte

class Kasse:
    def __init__(self, Lottokarten):
        self.Lottokarten = Lottokarten

        # Vorname
        while True:
            self.vorname = input("Gebe deinen Vornamen ein: ")
            print(f"Dein Vorname ist: {self.vorname}. Richtig? (ja/nein)")
            if input().lower() == "ja":
                break

        # Nachname
        while True:
            self.nachname = input("Gebe deinen Nachnamen ein: ")
            print(f"Dein Nachname ist: {self.nachname}. Richtig? (ja/nein)")
            if input().lower() == "ja":
                break

        # Adresse
        while True:
            self.adresse = input("Wie lautet deine Adresse? ")
            print(f"Deine Adresse ist: {self.adresse}. Richtig? (ja/nein)")
            if input().lower() == "ja":
                break

        # Postleitzahl
        while True:
            try:
                self.postleitzahl = int(input("Wie lautet deine Postleitzahl? "))
                print(f"Deine Postleitzahl ist: {self.postleitzahl}. Richtig? (ja/nein)")
                if input().lower() == "ja":
                    break
            except ValueError:
                print("Bitte gib eine gültige Zahl für die Postleitzahl ein.")

        # E-Mail
        while True:
            self.email = input("Wie lautet deine E-Mail-Adresse? ")
            print(f"Deine E-Mail ist: {self.email}. Richtig? (ja/nein)")
            if input().lower() == "ja":
                break

        # Altersabfrage
        while True:
            print("\nSind Sie mindestens 18 Jahre alt? (ja/nein)")
            self.alter_bestaetigt = input().lower()
            if self.alter_bestaetigt == "ja":
                break
            elif self.alter_bestaetigt == "nein":
                print("Teilnahme nicht möglich. Sie müssen mindestens 18 Jahre alt sein.")
                continue
            else:
                print("Bitte geben Sie 'ja' oder 'nein' ein.")

        # Gesamtdaten anzeigen
        print("\nZusammenfassung deiner Eingaben:")
        print("Vorname:", self.vorname)
        print("Nachname:", self.nachname)
        print("Adresse:", self.adresse)
        print("Postleitzahl:", self.postleitzahl)
        print("E-Mail:", self.email)
        print("Mindestens 18 Jahre alt:", self.alter_bestaetigt)
        print(f"Vielen Dank! Deine Daten wurden gespeichert und du musst insgesamt {1.20 * len(self.Lottokarten):.2f} € zahlen.")

# Objekt erzeugen (Beispiel)
#k = Kasse([])