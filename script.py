#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen Taschenrechner mit ausgelagerten Funktionen.

# 1. Erstellen Sie für jede der Grundrechenarten (Addition, Subtraktion, Multiplikation, Division) eine separate Funktion.
#    - Jede Funktion sollte zwei Argumente (Zahlen) als Eingabe akzeptieren und das Ergebnis der Berechnung zurückgeben.
#    - Die Funktionen sollten klar benannt und gemäß PEP8 formatiert sein.

# 2. Implementieren Sie eine Hauptfunktion (main), die:
#    - Den Benutzer auffordert, zwei Zahlen einzugeben.
#    - Den Benutzer auffordert, die gewünschte Operation auszuwählen (Addition, Subtraktion, Multiplikation, Division).
#    - Die entsprechende Rechenfunktion aufruft und das Ergebnis ausgibt.
#    - Eine Fehlerbehandlung integriert, um ungültige Eingaben und Division durch Null zu vermeiden.

# 3. Stellen Sie sicher, dass Ihr Code PEP8-konform ist:
#    - Verwenden Sie vier Leerzeichen für Einrückungen.
#    - Fügen Sie Leerzeichen um Operatoren ein.
#    - Halten Sie Zeilenlängen unter 79 Zeichen.
#    - Schreiben Sie geeignete Kommentare und verwenden Sie docstrings für Funktionen.

# Beispielablauf:
# - Der Benutzer gibt die Zahlen 10 und 5 ein.
# - Der Benutzer wählt die Operation 'Multiplikation'.
# - Die Funktion zur Multiplikation wird aufgerufen und das Ergebnis (50) wird ausgegeben.

# Optional: 
# - Fügen Sie weitere Funktionen hinzu, wie z.B. Potenzierung oder Modulo.
# - Implementieren Sie eine Schleife, um mehrere Berechnungen hintereinander durchzuführen, bis der Benutzer das Programm beendet.

def addition(number1: float, number2: float) -> float:
    "Führt die Addition von zwei Zahlen durch."
    return number1 + number2

def subtraction(number1: float, number2: float) -> float:
    "Führt die Subtraktion von zwei Zahlen durch."
    return number1 - number2

def multiplication(number1: float, number2: float) -> float:
    "Führt die Multiplikation von zwei Zahlen durch."
    return number1 * number2

def division(number1: float, number2: float) -> float:
    "Führt die Division von zwei Zahlen durch. Vermeidet Division durch Null."
    if number2 == 0:
        print("Fehler: Division durch Null ist nicht erlaubt.")
        return None
    return number1 / number2

def main():
    "Hauptfunktion, die den Benutzer durch die Berechnungen führt."
    try:
        number1 = float(input("Geben Sie die erste Zahl ein: "))
        number2 = float(input("Geben Sie die zweite Zahl ein: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie gültige Zahlen ein.")
        return
    
    print("Wählen Sie die Operation:")
    print("+: Addition")
    print("-: Subtraktion")
    print("*: Multiplikation")
    print("/: Division")

    operation = input("Geben Sie die Nummer der gewünschten Operation ein: ")
    
    if operation == "+":
        result = addition(number1, number2)
    elif operation == "-":
        result = subtraction(number1, number2)
    elif operation == "*":
        result = multiplication(number1, number2)
    elif operation == "/":
        result = division(number1, number2)
    else:
        print("Ungültige Operation. Bitte wählen Sie eine gültige Operation.")
        return
    
    if result is not None:
        print(f"Das Ergebnis der {operation} Operation von {number1} und {number2} ist: {result}")
        
if __name__ == "__main__":
    while True:
        main()
        cont = input("Möchten Sie eine weitere Berechnung durchführen? (ja/nein): ")
        if cont.lower() != "ja":
            print("Programm wird beendet.")
            break
