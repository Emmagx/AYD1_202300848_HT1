from fastapi import FastAPI

app = FastAPI()

@app.get("/cancion")
def get_cancion():
    return {"cancion": "Enamorado tuyo - Cuarteto de Nos"}