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
    """Relationships"""
    tracks = relationship('Track', back_populates='artists')

class Genre(Base):
    __tablename__ = "Genre"
    ID = sa.Column(sa.Integer, primary_key=True, name="ID")
    name = sa.Column(sa.String(100), nullable=False, name="Name")

class ArtistRelatedGenre(Base):
    __tablename__ = "ArtistRelatedGenre"
    ID = sa.Column(sa.Integer(), primary_key=True, index=True, nullable=False, name='ID')
    artist_id = sa.Column(sa.Integer(), sa.ForeignKey("Artist.ID"), nullable=False, name='ArtistID')
    genre_id = sa.Column(sa.Integer(), sa.ForeignKey("Genre.ID"), nullable=False, name='GenreID')
    
class Album(Base):
    __tablename__ = "Album"
    ID = sa.Column(sa.Integer, primary_key=True, name="ID")
    title = sa.Column(sa.String(100), nullable=False, name="Title")
    music_label = sa.Column(sa.String(200), nullable=False, name="MusicLabel")
    popularity = sa.Column(sa.Integer, nullable=False, name="Popularity")
    release_date = sa.Column(sa.String(100), nullable=False, name="ReleaseDate")
    total_tracks = sa.Column(sa.Integer, nullable=False, name="TotalTracks")
    type = sa.Column(sa.String(100), nullable=False, name="Type")
    """Relationships"""
    tracks = relationship('Track', back_populates='album')
    
class ArtistRelatedAlbum(Base):
    __tablename__ = "ArtistRelatedAlbum"
    ID = sa.Column(sa.Integer(), primary_key=True, nullable=False, name='ID')
    atrist_id = sa.Column(sa.Integer(), nullable=False, name='ArtistID')
    album_id = sa.Column(sa.Integer(), nullable=False, name='AlbumID')
    
class Track(Base):
    __tablename__ = "Track"
    ID = sa.Column(sa.Integer(), primary_key=True, nullable=False, name='ID')
    title = sa.Column(sa.String(200), nullable=False, name="Title")
    duration_ms = sa.Column(sa.Integer(), nullable=False, name="DurationMS")
    explicit = sa.Column(sa.Boolean(), nullable=False, name="Explicit")
    track_id = sa.Column(sa.String(100), nullable=False, name="TrackID")
    spotify_url = sa.Column(sa.String(150), nullable=False, name="SpotifyURL")
    album_id = sa.Column(sa.Integer(), sa.ForeignKey('Album.ID'), nullable=False, name="AlbumID") 
    artist_id = sa.Column(sa.Integer(), sa.ForeignKey('Artist.ID'), nullable=False, name="ArtistID")
    
    """Relationships"""
    artist = relationship('Artist', back_populates='tracks')
    album = relationship('Album', back_populates='tracks')
