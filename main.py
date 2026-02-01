from fastapi import FastAPI
import requests

app = FastAPI()
API_URL = "https://swapi.dev/api/"

@app.get("/api/healthcheck")
def healthcheck():
    return {"message": "Processo Seletivo - PowerOfData | Case Técnico: Avaliação para Cargo de Desenvolvedor Back End Python"}

@app.get("/")
async def get_root():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    return {"message": "Failed to fetch API data"}