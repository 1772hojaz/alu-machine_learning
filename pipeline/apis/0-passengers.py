#!/usr/bin/env python3

"""
 By using the Swapi API, create a method that returns the list of ships that can hold a given number of passengers:

Prototype: def availableShips(passengerCount):
Don’t forget the pagination
If no ship available, return an empty list.
"""

def availableShips(passengerCount):
    link = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

