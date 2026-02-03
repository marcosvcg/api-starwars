''' Recursos fornecidos hoje (03/02/2026) pela SWAPI '''

from api.base import BaseModel
from enum import StrEnum

class Resources(StrEnum):
    PEOPLE = "people"
    FILMS = "films"
    STARSHIPS = "starships"
    VEHICLES = "vehicles"
    SPECIES = "species"
    PLANETS = "planets"


class Person(BaseModel):
    pass


class Film(BaseModel):
    pass


class Starship(BaseModel):
    pass


class Vehicle(BaseModel):
    pass


class Specie(BaseModel):
    pass


class Planet(BaseModel):
    pass
