#!/usr/bin/env python3

"""
 By using the Swapi API, create a method that returns
 the list of ships that can hold a given
 number of passengers:
 Prototype: def availableShips(passengerCount):
 Don’t forget the pagination
 If no ship available, return an empty list.

"""
import requests as res


def availableShips(passengerCount):
    """
    Prototype: def availableShips(passengerCount):
    Don’t forget the pagination
    If no ship available, return an empty list.
    """
    link = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while link:
        response = res.get(link)
        data = response.json()
        for ship in data["results"]:
            if all((
                    ship["passengers"] != "n/a",
                    ship["passengers"] != "unknown",
                    ship["passengers"] != "0",
                    ship["passengers"] != "none"
                    )):
                ship["passengers"] = ship["passengers"].replace(",", "")
                if int(ship["passengers"]) >= passengerCount:
                    ships.append(ship["name"])
        link = data["next"]
    return ships
