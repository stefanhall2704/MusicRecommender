from src.utils.models import Artist, Genre, ArtistRelatedGenre
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from src.utils.dependency import get_db
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix="/api/album",
    tags=["Album"],
)

