from src.utils.models import Genre
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from src.utils.dependency import get_db
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/genre",
    tags=["Genre"],
)

class GenreRequest(BaseModel):
    name: str

async def get_genre_from_db(database: Session, genre_id: int):
    database_genre = (
        database.query(Genre)
        .filter(Genre.ID == genre_id)
        .first()
    )
    if not database_genre:
        raise Exception
    return database_genre

async def create_db_genre(
    database: Session,
    name: str,
):
    database_genre = Genre()
    database_genre.name = name
    database.add(database_genre)
    database.commit()
    return database_genre


# region endpoints.post
@router.post(
    "/create",
)
async def create_genre(
    genre_request: GenreRequest, database: Session = Depends(get_db)
):
    genre = await create_db_genre(
        database=database,
        name=genre_request.name
    )
    return genre

@router.delete("/delete")
async def delete_genre(
    genre_id: int,
    database: Session = Depends(get_db)
):
    genre = await get_genre_from_db(database=database, genre_id=genre_id)
    name = genre.name
    database.delete(genre)
    database.commit()
    return {"genre_name": name}