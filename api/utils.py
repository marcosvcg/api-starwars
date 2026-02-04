from fastapi import HTTPException
import requests
import math

def query(url: str, params: dict | None = None):
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Resource not found."
        )
    return response

def build_params(**kwargs):
    return {k: v for k, v in kwargs.items() if v is not None}

def paginate_data(data: dict, page: int) -> dict:
    total_pages = math.ceil(data['count'] / 10)
    data["next"] = page + 1 if page < total_pages else None
    data["previous"] = page - 1 if page > 1 else None
    return data