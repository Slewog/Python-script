#!/usr/bin/python3
# _*_ coding: utf-8_*_

def calculeHauteur(nombreMarches, hauteurMarche, nombreTrajets):
    hauteurMarche = hauteurMarche / 100 #conversion en metre
    unTrajet = nombreMarches * hauteurMarche
    hauteurJour = (unTrajet * 2) * nombreTrajets
    hauteurSemaine = hauteurJour * 7
    return hauteurSemaine

### Code
nombreTrajets = int(input("Combien de trajets : "))
nombreMarches = int(input("Combien de Marches : "))
hauteurMarche = float(input("Hauteur d'une marche en 'cm' : "))

hauteurSemaine = calculeHauteur(nombreMarches, hauteurMarche, nombreTrajets)
hauteurSemaine = round(hauteurSemaine, 2)
print(str(hauteurSemaine) + " mètres")
