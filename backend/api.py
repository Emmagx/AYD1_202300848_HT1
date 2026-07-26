from fastapi import FastAPI

app = FastAPI()

@app.get("/cancion")
def get_cancion():
    return {"album": "Porfiado- Cuarteto de Nos"}

@app.get("/album")
def get_album():
    return {"cancion": "Inverno del 92 - Cuarteto de nos"}