#!/usr/bin/python3
# -*-coding:Utf-8 -*

def table(nb):
    i = 1

    while i <= 10:
        print(i, "*", nb, "=", i * nb)
        i += 1

nb = input("Entrez un entier: ")
nb = int(nb)
table(nb)
