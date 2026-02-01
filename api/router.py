from fastapi import APIRouter
from api.utils import query

router = APIRouter()
API_URL = "https://swapi.dev/api/"

def _fetch(resource, id):
    result = query("{0}/{1}/{2}".format(
        API_URL,
        resource,
        str(id))
    )
    return result

@router.get("/people/{id}")
async def get_people(id):
    result = _fetch("people", id)
    return result.json()
