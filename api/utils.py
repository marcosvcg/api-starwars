from fastapi import HTTPException
import requests

def query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.get(query, headers=headers)
    if response.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="Resource not found."
        )
    return response