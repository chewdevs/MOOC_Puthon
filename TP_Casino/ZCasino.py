#!/usr/bin/python3
# -*-coding:Utf-8 -*

from math import ceil
from random import randrange

def pair(num):
    if num % 2 == 0:
        return True
    else:
        return False


def tirage(mise,num_mise):
    num_tire = randrange(50)
    print("Le numéro tiré est le : ", num_tire)
    if num_tire == num_mise:
        gain = mise + mise * 3
        print("Les numéros sont identiques")
        print("Bravo, vous avez gagné tois votre mise, soit: ",gain)
    elif ( pair(num_mise) is True and pair(num_tire) is True ) or ( pair(num_mise) is False and pair(num_tire) is False ):
        gain = mise + ceil(mise / 2)
        print("Les numéros sont de la même couleur")
        print("Bravo, vous avez gagné la moitié de votre mise, soit: ",gain)
    else:
        gain = -1 * mise
        print("Désolé, vous avez perdu")
    return gain


print("Bienvenue au casino, de quelle somme disposez vous ?")
somme = input("Entrez une somme d'argent en $: ")
somme = int(somme)

while somme > 0:
    mise = input("Entrez une somme à miser: ")
    try:
        mise = int(mise)
        assert mise <= somme
    except AssertionError:
        print("Votre mise est supérieure à votre somme initiale")
    else:
        num_mise = input("Entrez un numéro entre 0 et 50 sur lequel miser: ")
        try:
            num_mise = int(num_mise)
            assert num_mise >=0 and num_mise <=50
        except AssertionError:
            print("Votre numéro doit être compris entre 0 et 50")
        else:
            somme = somme + tirage(mise,num_mise)
    print("Voici votre somme restante en $: ",somme)
