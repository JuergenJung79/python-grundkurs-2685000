#!/usr/bin/env python3

# Eingaben über die Kommandozeile
# Einlesen eines Strings
name = input("Bitte geben Sie Ihren Namen ein: ")
print("Hallo, " + name + "!")

# Einlesen eines Integers und Umwandlung
alter = input("Bitte geben Sie Ihr Alter ein: ")
alter = int(alter)
print("Sie sind", alter, "Jahre alt.")
print("Sie sind " + str(alter) + " Jahre alt.")

# Berechnung mit der Eingabe
jahre_bis_30 = 30 - alter
if jahre_bis_30 > 0:
    print("In " + str(jahre_bis_30) + " Jahren werden Sie 30.")
else:
    print("Sie sind bereits 30 Jahre alt oder älter.")
    
# Aufgabe:
# Schreiben Sie ein Skript, das den Benutzer nach seinem Lieblingsfilm fragt
# und nach seiner Lieblingszahl. Addieren Sie 14.5 zu dieser Zahl. Geben Sie 
# dann eine personalisierte Nachricht aus, die diese Informationen enthält.
libelingsfilm = input("Bitte geben sie den Titel ihres Lieblingsfilms ein: ")
lieblingszahl = input("Bitte geben sie ihre Lieblingszahl ein: ")

neue_zahl = float(lieblingszahl) + 14.5
print("Ihr Lieblingsfilm ist " + libelingsfilm + " und Ihre Lieblingszahl plus 14.5 ist " + str(neue_zahl) + ".")

