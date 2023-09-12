import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()

class Artist(Base):
    __tablename__ = "Artist"
    ID = sa.Column(sa.Integer, primary_key=True, index=True, nullable=False, name="ID")
    name = sa.Column(sa.String(50), nullable=False, name="Name")
    artist_id = sa.Column(sa.String(100), nullable=False, name="ArtistID")
    followers = sa.Column(sa.Integer, nullable=False, name="Followers")
    genre = sa.Column(sa.Integer, name="Genre")
    popularity = sa.Column(sa.Integer, nullable=False, name="Popularity")