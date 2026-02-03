''' Recursos fornecidos hoje (03/02/2026) pela SWAPI '''

from api.base import BaseModel, BaseQuerySet
from enum import StrEnum

class Resources(StrEnum):
    PEOPLE = "people"
    FILMS = "films"
    STARSHIPS = "starships"
    VEHICLES = "vehicles"
    SPECIES = "species"
    PLANETS = "planets"


class Person(BaseModel):
    def get_starships(self):
        return StarshipQuerySet(self.starships)

class PersonQuerySet(BaseQuerySet):
    model = Person


class Film(BaseModel):
    pass

class FilmQuerySet(BaseQuerySet):
    model = Film


class Starship(BaseModel):
    pass

class StarshipQuerySet(BaseQuerySet):
    model = Starship


class Vehicle(BaseModel):
    pass

class VehicleQuerySet(BaseQuerySet):
    model = Vehicle


class Specie(BaseModel):
    pass

class SpecieQuerySet(BaseQuerySet):
    model = Specie


class Planet(BaseModel):
    pass

class PlanetQuerySet(BaseQuerySet):
    model = Planet