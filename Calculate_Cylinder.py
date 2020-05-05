#!/usr/bin/python3
from math import pi, sqrt

# Set this variable to 0 to enter the loop
choice = 0


def cylinder_calculate_volume(radius, height):
    volume = (pi * radius * radius * height)
    print("Votre volume sera de ", str(volume), " cm³")


def cylinder_calculate_radius(capacity, height):
    radius = sqrt(capacity / (pi * height))
    print("rayon = " + str(radius) + " cm pour un Diamètre total de " + str(radius * 2) + " cm")


while choice != 1 or 2:
    choice = int(input("Tappez '1' pour calculer un Volume et '2' pour calculer un rayon de contenant : "))
    if choice == 1:
        radius_input = float(input("Veuillez entrer le rayon en cm : "))
        height_input = float(input("Veuillez entrer la hauteur en cm : "))
        cylinder_calculate_volume(radius_input, height_input)
    elif choice == 2:
        capacity_input = float(input("Veuillez entrer la capacité voulue en Litre : "))
        height_input = float(input("Veuillez entrer la hauteur en cm : "))
        cylinder_calculate_radius(capacity_input / 0.001, height_input)
    else:
        print("Vous n'avez pas entrer un choix existant. Recommencer")