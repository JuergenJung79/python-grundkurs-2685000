#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Beispiel für argparse")
parser.add_argument("pflicht_int", help="Integer der erforderlich ist", type=int)
parser.add_argument("--optional_int", help="Optionaler Integer", type=int)
parser.add_argument("--optional_str", help="Optionaler String")
parser.add_argument("--wahl", help="Meine Wahl", choices=["a", "b", "c", "d"])
args = parser.parse_args()

print("Integer:", args.pflicht_int, "- Typ:", type(args.pflicht_int))
print("Optionaler Integer:", args.optional_int)
print("Optionaler String:", args.optional_str)
print("Wahl:", args.wahl)
print('ende')