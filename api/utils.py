from fastapi import HTTPException
import requests

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