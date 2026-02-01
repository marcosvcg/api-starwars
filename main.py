from fastapi import FastAPI
from api.router import router

app = FastAPI()
app.include_router(router)

@app.get("/api/healthcheck")
def healthcheck():
    return {"message": "Processo Seletivo - PowerOfData | Case Técnico: Avaliação para Cargo de Desenvolvedor Back End Python"}