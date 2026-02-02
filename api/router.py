from fastapi import APIRouter
from api.utils import query
from api import resources
import math

router = APIRouter()
API_URL = "https://swapi.dev/api/"

def _fetch(resource: resources, id):
    result = query("{0}/{1}/{2}".format(
        API_URL,
        resource,
        str(id))
    )
    return result

@router.get("/{resource}")
async def get_all_resource_data(
    resource,
    page: int = 1,
    search: str | None = None
):
    url = f"{API_URL}/{resource}/"

    params = {
        "page": page
    }

    if search:
        params["search"] = search

    result = query(url, params=params)
    data = result.json()

    pages = math.ceil(data['count'] / 10)
    data["next"] = page + 1 if page < pages else None
    data["previous"] = page - 1 if page > 1 else None

    return data

@router.get("/person/{id}")
async def get_person(id):
    result = _fetch(resources.PEOPLE, id)
    return result.json()

@router.get("/film/{id}")
async def get_film(id):
    result = _fetch(resources.FILMS, id)
    return result.json()

@router.get("/starship/{id}")
async def get_starship(id):
    result = _fetch(resources.STARSHIPS, id)
    return result.json()

@router.get("/vehicle/{id}")
async def get_vehicle(id):
    result = _fetch(resources.VEHICLES, id)
    return result.json()

@router.get("/specie/{id}")
async def get_species(id):
    result = _fetch(resources.SPECIES, id)
    return result.json()

@router.get("/planet/{id}")
async def get_planet(id):
    result = _fetch(resources.PLANETS, id)
    return result.json()