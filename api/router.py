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
async def get_person(id):
    result = _fetch(Resources.PEOPLE, id)
    return Person(result.content)

@router.get("/person/{id}/starships")
async def person_starships(id: int):
    person = await get_person(id)
    starships = person.get_starships()
    return starships.to_list()

@router.get("/film/{id}")
async def get_film(id):
    result = _fetch(Resources.FILMS, id)
    return Film(result.content)

@router.get("/starship/{id}")
async def get_starship(id):
    result = _fetch(Resources.STARSHIPS, id)
    return Starship(result.content)

@router.get("/vehicle/{id}")
async def get_vehicle(id):
    result = _fetch(Resources.VEHICLES, id)
    return Vehicle(result.content)

@router.get("/specie/{id}")
async def get_species(id):
    result = _fetch(Resources.SPECIES, id)
    return Specie(result.content)

@router.get("/planet/{id}")
async def get_planet(id):
    result = _fetch(Resources.PLANETS, id)
    return Planet(result.content)