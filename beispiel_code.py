#!/usr/bin/env python3

# Einführung in Klassen in Python

class Buch:
    """Eine einfache Klasse zur Darstellung eines Buches im Bücherregal."""
    
    def __init__(self, titel: str, autor: str):
        """Initialisiert das Buch mit einem Titel und einem Autor."""
        self.titel = titel # Öffentliches Attribut
        self.autor = autor # Öffentliches Attribut
        self._status = "verfügbar" # Nicht öffentliches Attribut, das den Ausleihstatus des Buches angibt
        
    def ausleihen(self):
        """Markiert das Buch als ausgeliehen, wenn es verfügbar ist."""
        if self._status == "verfügbar":
            self._status = "ausgeliehen"
            print(f"Das Buch '{self.titel}' wurde ausgeliehen.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits ausgeliehen.")
            
    def zurückgeben(self):
        """Markiert das Buch als verfügbar."""
        if self._status == "ausgeliehen":
            self.status = "verfügbar"
            print(f"Das Buch '{self.titel}' wurde zurückgegeben.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits verfügbar.")
    
    def get_status(self) -> str:
        """Gibt den aktuellen Ausleihstatus des Buches zurück."""
        return self._status
    
class Bücherregal:
    """Eine Klasse zur Verwaltung eines Bücherregals."""
    
    def __init__(self):
        """Initialisiert das Bücherregal als leeres Regal."""
        self._bücher = [] # Privates Attribut, das eine Liste von Büchern speichert
        
    def buch_hinzufügen(self, buch: Buch):
        """Fügt ein Buch zum Bücherregal hinzu."""
        self._bücher.append(buch)
        print(f"Das Buch '{buch.titel}' wurde dem Regal hinzugefügt.")
        
    def buch_entfernen(self, buch: Buch):
        """Entfernt ein Buch aus dem Bücherregal."""
        if buch in self._bücher:
            self._bücher.remove(buch)
            print(f"Das Buch '{buch.titel}' wurde aus dem Regal entfernt.")
        else:
            print(f"Das Buch '{buch.titel}' ist nicht im Regal.")
            
    def alle_bücher_anzeigen(self):
        """Zeigt alle Bücher im Bücherregal an."""
        if self._bücher:
            print("Bücher im Regal:")
            for buch in self._bücher:
                status = buch.get_status()
                print(f" - {buch.titel} von {buch.autor} (Status: {status})")
        else:
            print("Das Regal ist leer.")
            
# Erstellung von Büchern
buch1 = Buch("Der Hobbit", "J.R.R. Tolkien")
print("Titel lautet", buch1.titel) # Zugriff auf das öffentliche Attribut 'titel'
buch2 = Buch("1984", "George Orwell")
print("Autor lautet", buch2.autor) # Zugriff auf das öffentliche Attribut 'autor'
print("Satus lautet", buch2.get_status()) # Zugriff auf den Status über die Methode get_status()

regal = Bücherregal()
regal.buch_hinzufügen(buch1)
regal.buch_hinzufügen(buch2)

regal.alle_bücher_anzeigen()
buch1.ausleihen()
regal.alle_bücher_anzeigen()

print("")
print("Ab hier startet die Aufgabe für das Thema Klassen in Python")
print("===========================================================")
print("")

# Aufgabe:
# Erstellen Sie eine Klasse 'Ebike', die die Eigenschaften 'marke', 'modell' und 'reichweite' hat.
# - Implementieren Sie eine Methode 'tanken', die die Reichweite um einen gegebenen Wert erhöht.
# - Stellen Sie sicher, dass der Tankinhalt privat ist und nur über eine Methode abgefragt werden kann.
# - Instanzieren Sie ein Elektrofahrrad und testen Sie die Methoden.

class Ebike:
    """Eine Klasse zur Darstellung eines Elektrofahrrads."""
    
    def __init__(self, marke: str, modell: str, reichweite: int):
        """Initialisiert das Ebike mit Marke, Modell und Reichweite."""
        self.marke = marke # Öffentliches Attribut
        self.modell = modell # Öffentliches Attribut
        self.reichweite = reichweite # Öffentliches Attribut
        self._tankinhalt = 0 # Privates Attribut, das den aktuellen Tankinhalt in Prozent angibt
        
    def tanken(self, menge: int):
        """Erhöht die Reichweite um einen gegebenen Wert, ohne 100% zu überschreiten."""
        if menge < 0:
            print("Die Menge zum Tanken muss positiv sein.")
            return
        self._tankinhalt += menge
        if self._tankinhalt > 100:
            self._tankinhalt = 100
        print(f"Das Ebike wurde getankt. Aktueller Tankinhalt: {self._tankinhalt}%")
        
    def get_tankinhalt(self) -> int:
        """Gibt den aktuellen Tankinhalt zurück,"""
        return self._tankinhalt
    
fahrrad1 = Ebike("Giant", "Explore E+ 2", 80)
print(f"Marke: {fahrrad1.marke}, Modell: {fahrrad1.modell}, Reichweite: {fahrrad1.reichweite} km")
fahrrad1.tanken(30) # Versuch, das Ebike um 30% zu tanken
fahrrad1.tanken(50) # Versuch, das Ebike um 50% zu tanken
fahrrad1.tanken(50) # Versuch, das Ebike um 50% zu tanken
print(f"Aktueller Tankinhalt: {fahrrad1.get_tankinhalt()}%") # Abfrage des aktuellen Tankinhalts
