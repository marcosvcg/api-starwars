from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["https://www.powerofdata.ai", "http://localhost:5173"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)

@app.get("/api/healthcheck")
def healthcheck():
    return {"message": "Processo Seletivo - PowerOfData | Case Técnico: Avaliação para Cargo de Desenvolvedor Back End Python"}