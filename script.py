#!/usr/bin/env python3

import argparse

# Aufgabe: Erstellen Sie ein Skript, das einfache mathematische Operationen basierend auf Befehlszeilenargumenten durchführt.

# 1. Das Skript soll zwei Pflichtargumente akzeptieren, die als ganze Zahlen eingegeben werden.
#    - 'zahl1': Die erste Zahl, die verwendet wird.
#    - 'zahl2': Die zweite Zahl, die verwendet wird.

parser = argparse.ArgumentParser(description="Einfaches Beispiel bzw. Aufgabe für die Verwendung von argparse.")
parser.add_argument("zahl1", type=int, help="Die erste Zahl")
parser.add_argument("zahl2", type=int, help="Die zweite Zahl")

# 2. Es soll ein optionales Argument '--operation' geben, das die gewünschte mathematische Operation festlegt:
#    - Mögliche Optionen: 'add' (Addition), 'sub' (Subtraktion), 'mul' (Multiplikation), 'div' (Division).
#    - Wenn keine Operation angegeben wird, soll standardmäßig die Addition ausgeführt werden.
parser.add_argument("--operation", choices=["add", "sub", "mul", "div"], default="add", help="Die auszuführende Operation (add, sub, mul, div)")

args = parser.parse_args()

# 3. Implementieren Sie die Berechnungslogik für die oben genannten Operationen:
#    - Bei der Division soll eine Fehlerbehandlung implementiert werden, um eine Division durch Null zu vermeiden.
if args.operation == "add":
    ergebnis = args.zahl1 + args.zahl2
    
elif args.operation == "sub":
    ergbenis = args.zahl1 - args.zahl2
    
elif args.operation == "mul":
    ergebnis = args.zahl1 * args.zahl2
    
elif args.operation == "div":
    if args.zahl2 != 0:
        ergebnis = args.zahl1 / args.zahl2
    else:
        ergebnis = "Fehler: Division durch Null ist nicht erlaubt."

# 4. Geben Sie das Ergebnis der Berechnung aus.
print("Das Ergebnis ist:", ergebnis)