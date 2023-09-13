import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import UniqueConstraint

Base = declarative_base()

class Artist(Base):
    __tablename__ = "Artist"
    ID = sa.Column(sa.Integer, primary_key=True, index=True, nullable=False, name="ID")
    name = sa.Column(sa.String(50), nullable=False, name="Name")
    artist_id = sa.Column(sa.String(100), unique=True, nullable=False, name="ArtistID")
    followers = sa.Column(sa.Integer, nullable=False, name="Followers")
    genre = sa.Column(sa.Integer, name="Genre")
    popularity = sa.Column(sa.Integer, nullable=False, name="Popularity")
    __table_args__ = (
        UniqueConstraint('ArtistID', name='unique_artist_id'),
    )

class Genre(Base):
    __tablename__ = "Genre"
    ID = sa.Column(sa.Integer, primary_key=True, name="ID")
    name = sa.Column(sa.String(100), nullable=False, name="Name")

class ArtistRelatedGenre(Base):
    __tablename__ = "ArtistRelatedGenre"
    ID = sa.Column(sa.Integer(), primary_key=True, index=True, nullable=False, name='ID')
    artist_id = sa.Column(sa.Integer(), sa.ForeignKey("Artist.ID"), nullable=False, name='ArtistID')
    genre_id = sa.Column(sa.Integer(), sa.ForeignKey("Genre.ID"), nullable=False, name='GenreID')