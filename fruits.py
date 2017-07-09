#!/usr/bin/python3
# -*-coding:Utf-8 -*

inventaire = [("pommes", 22),("melons", 4),("poires", 18),("fraises", 76),("prunes", 51),]

fruits_ranges = sorted([(nb_fruits,fruits) for (fruits,nb_fruits) in inventaire],reverse=True)
inventaire = [(fruits,nb_fruits) for (nb_fruits,fruits) in fruits_ranges]

print(inventaire)
