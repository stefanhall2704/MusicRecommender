from src.utils.models import Artist, Genre, ArtistRelatedGenre
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
    genre: list
    

async def get_artist_from_db(database: Session, artist_id: int):
    database_artist = (
        database.query(Artist)
        .filter(Artist.ID == artist_id)
        .first()
    )
    if not database_artist:
        raise Exception
    return database_artist

async def get_artist_from_db_by_artist_id(database: Session, artist_id: int):
    database_artist = (
        database.query(Artist)
        .filter(Artist.artist_id == artist_id)
        .first()
    )
    if not database_artist:
        raise Exception
    return database_artist

async def get_db_genre_related_artist(database: Session, id: int):
    database_artist = (
        database.query(ArtistRelatedGenre)
        .filter(ArtistRelatedGenre.ID == id)
        .first()
    )
    if not database_artist:
        raise Exception
    return database_artist

async def get_db_genre_by_name(databse: Session, genre: str):
    genre = genre.title()
    db_genre = (
        databse.query(Genre)
        .filter(Genre.name == genre)
        .first()
    )
    if not db_genre:
        return {"genre_error": "Genre Does not Exist"}
    return db_genre

async def create_db_genre_related_artist(
    database: Session,
    artist_id: int,
    genre_id: int
):

    database_genre_related_artist = ArtistRelatedGenre()
    database_genre_related_artist.artist_id = artist_id
    database_genre_related_artist.genre_id = genre_id
    database.add(database_genre_related_artist)
    database.commit()
    return database_genre_related_artist

async def create_db_artist(
    database: Session,
    name: str,
    artist_id: str,
    followers: int,
    popularity: int,
    genre: Optional[int]
):
    try:
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
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Artist with this name already exists")


# region endpoints.post
@router.post(
    "/create",
)
async def create_artist(
    artist_request: ArtistRequest, database: Session = Depends(get_db)
):
    artist_exists = (
        database.query(Artist)
        .filter(Artist.artist_id == artist_request.artist_id)
        .first()
    )
    if artist_exists:
        return {"message": "Artist with this name already exists"}
    genres = artist_request.genre
    artist_id = artist_request.artist_id
    await create_db_artist(database=database, 
        name=artist_request.name, 
        artist_id=artist_id, 
        followers=artist_request.followers,
        popularity=artist_request.popularity,
        genre=0
    )
    db_artist = await get_artist_from_db_by_artist_id(database=database, artist_id=artist_id)
    db_artist_id = db_artist.ID
    print(genres)
    for genre in genres:
        print(genre)
        db_genre = await get_db_genre_by_name(databse=database, genre=genre)        
        db_genre_id = db_genre.ID
        await create_db_genre_related_artist(database=database, artist_id=db_artist_id, genre_id=db_genre_id)
    return {"Done": "Success"}

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

@router.delete("/related/delete")
async def delete_related_artist(
    id: int,
    database: Session = Depends(get_db)
):
    artist = await get_db_genre_related_artist(database=database, id=id)
    database.delete(artist)
    database.commit()
    return {"Success"}