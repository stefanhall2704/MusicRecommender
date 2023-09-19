import uvicorn
from decouple import config
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from sqlalchemy.orm import Session
from starlette.requests import Request

from src.api import (
    artist,
    genre,
    album,
    track
)


from src.utils import models
from src.utils.database import engine



app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

models.Base.metadata.create_all(bind=engine)

app.include_router(artist.router)
app.include_router(genre.router)
app.include_router(album.router)
app.include_router(track.router)







if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=4000)