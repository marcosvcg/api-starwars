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
    def get_films(self):
        return FilmQuerySet(self.films)

    def get_vehicles(self):
        return VehicleQuerySet(self.vehicles)

    def get_starships(self):
        return StarshipQuerySet(self.starships)

class PeopleQuerySet(BaseQuerySet):
    model = Person


class Film(BaseModel):
    def get_characters(self):
        return PeopleQuerySet(self.characters)

    def get_planets(self):
        return PlanetQuerySet(self.planets)

    def get_species(self):
        return SpecieQuerySet(self.species)

class FilmQuerySet(BaseQuerySet):
    model = Film


class Starship(BaseModel):
    def get_pilots(self):
        return PeopleQuerySet(self.pilots)

    def get_films(self):
        return FilmQuerySet(self.films)

class StarshipQuerySet(BaseQuerySet):
    model = Starship


class Vehicle(BaseModel):
    def get_pilots(self):
        return PeopleQuerySet(self.pilots)

    def get_films(self):
        return FilmQuerySet(self.films)

class VehicleQuerySet(BaseQuerySet):
    model = Vehicle


class Specie(BaseModel):
    def get_people(self):
        return PeopleQuerySet(self.people)

class SpecieQuerySet(BaseQuerySet):
    model = Specie


class Planet(BaseModel):
    def get_residents(self):
        return PeopleQuerySet(self.residents)

    def get_films(self):
        return FilmQuerySet(self.films)

class PlanetQuerySet(BaseQuerySet):
    model = Planet