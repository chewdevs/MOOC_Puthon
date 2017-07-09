#!/usr/bin/python3
# -*-coding:Utf-8 -*

annee = input()
try: # On essaye de convertir l'année en entier
    annee = int(annee)
except:
    print("Erreur lors de la conversion de l'année.")
