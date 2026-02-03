from fastapi import APIRouter
from api.resources import Person, Film, Starship, Vehicle, Specie, Planet
from api.utils import query, build_params, paginate_data
from api.resources import Resources

router = APIRouter()
API_URL = "https://swapi.dev/api/"

def _fetch(resource: Resources, id: int):
    result = query(f"{API_URL}/{resource}/{id}")
    return result

@router.get("/{resource}")
async def get_all_resource_data(
    resource: Resources,
    page: int = 1,
    search: str | None = None
):
    url = f"{API_URL}/{resource}/"
    params = build_params(page=page, search=search)
    data = query(url, params=params).json()

    return paginate_data(data, page)

@router.get("/person/{id}")
async def get_person(id: int):
    result = _fetch(Resources.PEOPLE, id)
    return Person(result.content)

@router.get("/person/{id}/films")
async def get_person_films(id: int):
    person = await get_person(id)
    films = person.get_films()
    return films.to_list()

@router.get("/person/{id}/vehicles")
async def get_person_vehicles(id: int):
    person = await get_person(id)
    vehicles = person.get_vehicles()
    return vehicles.to_list()

@router.get("/person/{id}/starships")
async def get_person_starships(id: int):
    person = await get_person(id)
    starships = person.get_starships()
    return starships.to_list()


@router.get("/film/{id}")
async def get_film(id: int):
    result = _fetch(Resources.FILMS, id)
    return Film(result.content)

@router.get("/film/{id}/characters")
async def get_film_characters(id: int):
    film = await get_film(id)
    characters = film.get_characters()
    return characters.to_list()

@router.get("/film/{id}/planets")
async def get_film_planets(id: int):
    film = await get_film(id)
    planets = film.get_planets()
    return planets.to_list()

@router.get("/film/{id}/species")
async def get_film_species(id: int):
    film = await get_film(id)
    species = film.get_species()
    return species.to_list()


@router.get("/starship/{id}")
async def get_starship(id: int):
    result = _fetch(Resources.STARSHIPS, id)
    return Starship(result.content)

@router.get("/starship/{id}/pilots")
async def get_starship_pilots(id: int):
    starship = await get_starship(id)
    pilots = starship.get_pilots()
    return pilots.to_list()

@router.get("/starship/{id}/films")
async def get_starship_films(id: int):
    starship = await get_starship(id)
    films = starship.get_films()
    return films.to_list()


@router.get("/vehicle/{id}")
async def get_vehicle(id: int):
    result = _fetch(Resources.VEHICLES, id)
    return Vehicle(result.content)

@router.get("/vehicle/{id}/films")
async def get_vehicle_films(id: int):
    vehicle = await get_vehicle(id)
    films = vehicle.get_films()
    return films.to_list()

@router.get("/vehicle/{id}/pilots")
async def get_vehicle_pilots(id: int):
    vehicle = await get_vehicle(id)
    pilots = vehicle.get_pilots()
    return pilots.to_list()


@router.get("/specie/{id}")
async def get_specie(id: int):
    result = _fetch(Resources.SPECIES, id)
    return Specie(result.content)

@router.get("/specie/{id}/people")
async def get_specie_people(id: int):
    specie = await get_specie(id)
    people = specie.get_people()
    return people.to_list()


@router.get("/planet/{id}")
async def get_planet(id: int):
    result = _fetch(Resources.PLANETS, id)
    return Planet(result.content)

@router.get("/planet/{id}/residents")
async def get_planet_residents(id: int):
    planet = await get_planet(id)
    residents = planet.get_residents()
    return residents.to_list()

@router.get("/planet/{id}/films")
async def get_planet_films(id: int):
    planet = await get_planet(id)
    films = planet.get_films()
    return films.to_list()