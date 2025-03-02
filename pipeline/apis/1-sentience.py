#!/usr/bin/env python3
"""
By using the Swapi API, create a method that returns
the list of names of the home planets of all sentient species.

Prototype: def sentientPlanets():
Don’t forget the pagination
"""
import requests as res


def sentientPlanets():
    """
    Prototype: def sentientPlanets():
    Don’t forget the pagination

    """
    link = "https://swapi-api.hbtn.io/api/species/?format=json"
    speciesList = []
    while link:
        result = res.get(link).json()
        speciesList += result.get("results")
        link = result.get("next")

        homePlanets = []
        for i in speciesList:
            if i.get("designation") == "sentient" or \
             i.get("classification") == "sentient":
                link = i.get("homeworld")
                if link:
                    planet = res.get(link).json()
                    homePlanets.append(planet.get("name"))
        return homePlanets
