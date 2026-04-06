#!/usr/bin/env python3

# Aufgabe: Erstellen Sie ein Skript, das die Länge eines Textes analysiert und Informationen darüber liefert.

# Das Skript soll folgende Funktionalität bieten:
# 1. Ein Pflichtargument (positional argument), das einen Text entgegennimmt.
# 2. Ein optionales Argument --details, das zusätzliche Informationen liefert:
#    - Anzahl der Wörter
# 3. Wenn das Argument --details nicht angegeben wird, soll nur die Anzahl der Zeichen ausgegeben werden.

# Beispiel:
# python3 script.py "Dies ist ein Beispieltext." --details
# Ausgabe:
# Zeichen: 27
# Wörter: 5

# Optional: Erweitern Sie das Skript, um auch die Anzahl der Vokale und Konsonanten zu zählen.

import argparse

parser = argparse.ArgumentParser(description="Analysiere die Länge eines Textes und liefere Informationen darüber.")

parser.add_argument("text", type=str, help="Der Text, der analysiert werden soll.")
parser.add_argument("--details", action="store_true", help="Zusätzliche Informationen liefern.")

args = parser.parse_args()

text = args.text

# Zählen der Zeichen
char_count = len(text)
# Zählen der Wörter
word_count = len(text.split())

vokal_count = sum(1 for char in text if char.lower() in 'aeiou')
konsonant_count = sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')

print(f"Zeichen: {char_count}")

if args.details:   
    print(f"Wörter: {word_count}")
    print(f"Vokale: {vokal_count}")
    print(f"Konsonanten: {konsonant_count}")
