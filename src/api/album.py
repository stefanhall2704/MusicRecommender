from src.utils.models import Artist, Genre, ArtistRelatedGenre, Album, ArtistRelatedAlbum
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from src.utils.dependency import get_db
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/album",
    tags=["Album"],
)

class AlbumRequest(BaseModel):
    title: str
    music_label: str
    popularity: int
    release_date: str
    total_tracks: int
    type: str
    album_id: str
    artist_id: str
    
async def get_album_from_db_by_album_id(database: Session, album_id: int):
    database_album = (
        database.query(Album)
        .filter(Album.album_id == album_id)
        .first()
    )
    if not database_album:
        raise Exception
    return database_album

async def get_artist_from_db_by_artist_id(database: Session, artist_id: int):
    database_album = (
        database.query(Artist)
        .filter(Artist.artist_id == artist_id)
        .first()
    )
    if not database_album:
        raise Exception
    return database_album

async def get_related_album_from_db_by_album_id(database: Session, album_id: int):
    database_album = (
        database.query(ArtistRelatedAlbum)
        .filter(ArtistRelatedAlbum.album_id == album_id)
        .first()
    )
    if not database_album:
        raise Exception
    return database_album

async def get_album_from_db_by_id(database: Session, album_id: int):
    database_album = (
        database.query(Album)
        .filter(Album.ID == album_id)
        .first()
    )
    if not database_album:
        raise Exception
    return database_album

async def create_db_album(
    database: Session,
    title: str,
    music_label: str,
    popularity: int,
    release_date: str,
    total_tracks: int,
    type: str,
    album_id: str,
    artist_id: str
):
    database_album = Album()
    database_album.title = title
    database_album.music_label = music_label
    database_album.popularity = popularity
    database_album.release_date = release_date
    database_album.total_tracks = total_tracks
    database_album.type = type
    database_album.album_id = album_id
    database.add(database_album)
    database.commit()
    album = await get_album_from_db_by_album_id(database=database, album_id=album_id)
    db_album_id = album.ID
    db_artist = await get_artist_from_db_by_artist_id(database=database, artist_id=artist_id)
    db_artist_id = db_artist.ID
    database_artist_related_album = ArtistRelatedAlbum()
    database_artist_related_album.album_id = db_album_id
    database_artist_related_album.atrist_id = db_artist_id
    database.add(database_artist_related_album)
    database.commit()
    return {
        "album": database_album,
        "artist_related_album": database_artist_related_album
    }
    
    
@router.post("/create")
async def create_album(
    album_request: AlbumRequest,
    database: Session = Depends(get_db)
):
    try:
        db_album = await create_db_album(
            database=database,
            title=album_request.title,
            music_label=album_request.music_label,
            popularity=album_request.popularity,
            release_date=album_request.release_date,
            total_tracks=album_request.total_tracks,
            type=album_request.type,
            album_id=album_request.album_id,
            artist_id=album_request.artist_id
        )
        return db_album
    except Exception as e:
        print(e)
    
@router.delete("/delete")
async def delete_album(
    album_id: int,
    database: Session = Depends(get_db)
):
    db_album = await get_album_from_db_by_id(database=database, album_id=album_id)
    database.delete(db_album)
    database.commit()
    related_albums = await get_related_album_from_db_by_album_id(database=database, album_id=album_id)
    database.delete(related_albums)
    database.commit()
    return {"Success"}

