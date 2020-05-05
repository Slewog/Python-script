#!/usr/bin/python3
# _*_ coding: utf-8_*_


def calculate_distance(numbers_trips, numbers_steps, height_step):
    one_trips = numbers_steps * height_step
    distance_total = ((one_trips * 2) * numbers_trips) * 7
    return distance_total


# Code
numbers_trips_input = int(input("Combien de trajets par jour ? "))
numbers_steps_input = int(input("Combien de marches y a t'il ? "))
height_step_input = float(input("Hauteur d'une marche en 'cm' ? "))
distance_per_week = calculate_distance(numbers_trips_input, numbers_steps_input, height_step_input / 100)
print("Vous parcourez ", str(distance_per_week), " mètres par semaines")