from fastapi import FastAPI

app = FastAPI()

@app.get("/cancion")
def get_cancion():
    return {"album": "Porfiado- Cuarteto de Nos"}