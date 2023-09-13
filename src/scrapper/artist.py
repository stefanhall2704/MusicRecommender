from src.scrapper.spotify_data import SpotifyData, client_id, client_secret
from src.api.artist import create_artist
from src.utils.dependency import get_db
from fastapi import Depends
import requests
from src.api.genre import get_genre_from_db
import json

spotify = SpotifyData(client_id, client_secret)
database = Depends(get_db)

"""
Artist Metrics:
Name
Total Followers
Popularity
ID
Genres: Relate to table Genre ID
"""
# Number of artists you want to scrape
total_artists_to_scrape = 100


genres = requests.get("http://localhost:4000/api/genre/genres")

for genre in genres.json():
    genre = genre["name"]
    limit = 50
    offset = 1

    while offset < total_artists_to_scrape:
        results = spotify.sp.search(q=f'genre:{genre}', type="artist", limit=limit, offset=offset)

        for artist in results["artists"]["items"]:
            followers = artist["followers"]["total"]
            name = artist["name"]
            popularity = artist["popularity"]
            artist_id = artist["id"]
            genres = artist["genres"]
            json_body = {
                "name": name,
                "artist_id": artist_id,
                "followers": followers,
                "popularity": popularity,
                "genre": genres
            }
            requests.post("http://localhost:4000/api/artist/create", json=json_body)
            print(name)
        offset += limit        
