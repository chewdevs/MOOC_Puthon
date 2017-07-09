#!/usr/bin/python3
# -*-coding:Utf-8 -*

#Chargement de modules complémentairtes
import random
import pickle


#Chargement des fonctions du pendu
from fonctions import *


#Chargement des données
from donnees import *


#Importation des scores des joueurs
try:
    score_joueurs = import_score(fichier_scores)
except FileNotFoundError:
    score_joueurs = {}


print("Bienvenue dans le jeu de Pendu")
nom_joueur = input("Entrez votre nom: ")
for nom,score in score_joueurs.items():
    print("toto")
    if nom_joueur == nom:
        print("{}, votre score est de {}".format(nom,score))
    else:
        score_joueurs["nom_joueur"] = 0
        print("{}, votre score est de {}".format(nom_joueur,score_joueurs["nom_joueur"]))
# while continuer_partie:
