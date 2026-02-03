from fastapi import APIRouter
from api.utils import query, build_params
from api.resources import Resources
import math

router = APIRouter()
API_URL = "https://swapi.dev/api/"

def _fetch(resource: Resources, id):
    result = query("{0}/{1}/{2}".format(
        API_URL,
        resource,
        str(id))
    )
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

    total_pages = math.ceil(data['count'] / 10)
    data["next"] = page + 1 if page < total_pages else None
    data["previous"] = page - 1 if page > 1 else None

    return data

@router.get("/person/{id}")
async def get_person(id):
    result = _fetch(Resources.PEOPLE, id)
    return result.json()

@router.get("/film/{id}")
async def get_film(id):
    result = _fetch(Resources.FILMS, id)
    return result.json()

@router.get("/starship/{id}")
async def get_starship(id):
    result = _fetch(Resources.STARSHIPS, id)
    return result.json()

@router.get("/vehicle/{id}")
async def get_vehicle(id):
    result = _fetch(Resources.VEHICLES, id)
    return result.json()

@router.get("/specie/{id}")
async def get_species(id):
    result = _fetch(Resources.SPECIES, id)
    return result.json()

@router.get("/planet/{id}")
async def get_planet(id):
    result = _fetch(Resources.PLANETS, id)
    return result.json()