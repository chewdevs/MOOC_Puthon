#!/usr/bin/python3
# -*-coding:Utf-8 -*

def afficher_flottant(flottant):
    flottant = str(flottant)
    return flottant.split(".")[0] + "," + flottant.split(".")[1][:3]

print(afficher_flottant(3.999999999))
print(afficher_flottant(1.55555555))
