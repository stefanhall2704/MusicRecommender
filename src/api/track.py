from src.utils.models import Track, Album, Artist
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from src.utils.dependency import get_db
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/track",
    tags=["Track"],
)

class TrackRequest(BaseModel):
    title: str
    duration_ms: int
    explicit: bool
    track_id: str
    spotify_url: str
    album_id: str
    artist_id: str
    
async def get_track_from_db_by_track_id(database: Session, track_id: int):
    database_track = (
        database.query(Track)
        .filter(Track.track_id == track_id)
        .first()
    )
    if not database_track:
        raise Exception
    return database_track

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

async def get_track_from_db_by_id(database: Session, track_id: int):
    database_track = (
        database.query(Track)
        .filter(Track.ID == track_id)
        .first()
    )
    if not database_track:
        raise Exception
    return database_track

async def create_db_track(
    database: Session,
    title: str,
    duration_ms: int,
    explicit: bool,
    track_id: str,
    spotify_url: str,
    album_id: str,
    artist_id: str
):
    db_album = await get_album_from_db_by_album_id(database=database, album_id=album_id)
    db_artist = await get_artist_from_db_by_artist_id(database=database, artist_id=artist_id)
    db_artist_id = db_artist.ID
    db_album_id = db_album.ID
    database_track = Track()
    database_track.title = title
    database_track.duration_ms = duration_ms
    database_track.explicit = explicit
    database_track.track_id = track_id
    database_track.spotify_url = spotify_url
    database_track.artist_id = db_artist_id
    database_track.album_id = db_album_id
    database.add(database_track)
    database.commit()
    return database_track
    
@router.post("/create")
async def create_track(
    track_request: TrackRequest,
    database: Session = Depends(get_db)
):
    try:
        db_track = await create_db_track(
            database=database,
            title=track_request.title,
            duration_ms=track_request.duration_ms,
            explicit=track_request.explicit,
            track_id=track_request.track_id,
            spotify_url=track_request.spotify_url,
            album_id=track_request.album_id,
            artist_id=track_request.artist_id
        )
        return db_track
    except Exception as e:
        print(e)
    
@router.delete("/delete")
async def delete_track(
    track_id: int,
    database: Session = Depends(get_db)
):
    db_track = await get_track_from_db_by_id(database=database, track_id=track_id)
    database.delete(db_track)
    database.commit()
    return {"Success"}

