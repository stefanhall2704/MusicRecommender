from src.utils.models import Artist
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from src.utils.dependency import get_db
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/artist",
    tags=["Artist"],
)

class ArtistRequest(BaseModel):
    name: str
    artist_id: str
    followers: int
    popularity: int
    genre: Optional[int]
    

async def get_artist_from_db(database: Session, artist_id: int):
    database_artist = (
        database.query(Artist)
        .filter(Artist.ID == artist_id)
        .first()
    )
    if not database_artist:
        raise Exception
    return database_artist

async def create_db_artist(
    database: Session,
    name: str,
    artist_id: str,
    followers: int,
    popularity: int,
    genre: Optional[int]
):
    database_artist = Artist()
    database_artist.name = name
    database_artist.artist_id = artist_id
    database_artist.followers = followers
    database_artist.popularity = popularity
    if genre:
        database_artist.genre = genre
    database.add(database_artist)
    database.commit()
    return database_artist


# region endpoints.post
@router.post(
    "/create",
)
async def create_artist(
    artist_request: ArtistRequest, database: Session = Depends(get_db)
):
    artist = await create_db_artist(database=database, 
        name=artist_request.name, 
        artist_id=artist_request.artist_id, 
        followers=artist_request.followers,
        popularity=artist_request.popularity,
        genre=artist_request.genre 
    )
    return artist

@router.delete("/delete")
async def delete_artist(
    artist_id: int,
    database: Session = Depends(get_db)
):
    artist = await get_artist_from_db(database=database, artist_id=artist_id)
    name = artist.name
    database.delete(artist)
    database.commit()
    return {"name": name}