from src.scrapper.spotify_data import (SpotifyData, client_id, client_secret)
import json
from pydantic import BaseModel
import requests


spotify_data = SpotifyData(client_id=client_id, client_secret=client_secret)

def call_track(track, album_id: int, artist_id: int) -> None:
    title = track.get("name", "")
    duration_ms = track.get("duration_ms", 0)
    explicit = track.get("explicit", False)
    track_id = track.get("id", "")
    spotify_url = track["external_urls"]["spotify"]
    print(title)
    


def tracks(album_id: int, artist_id: int) -> None:
    album_tracks = spotify_data.get_album_tracks(album_id=album_id)
    tracks = album_tracks["items"]
    for track in tracks:
        call_track(track=track, album_id=album_id, artist_id=artist_id)
        

def call_album(album_id: int, artist_id: int):
    album_data = spotify_data.get_album_data(album_id=album_id)
    title = album_data.get("name", "")
    music_label = album_data.get("label", "")
    popularity = album_data.get("popularity", "")
    release_date = album_data.get("release_date", "")
    total_tracks = album_data.get("total_tracks", "")
    type = album_data.get("type")
    
    """
    Database functions
    """
    tracks(album_id=album_id, artist_id=artist_id)
    print(f"Album {title} added to the DB")


if __name__ == "__main__":
    artists = requests.get("http://localhost:4000/api/artist/limited_artists?limit=1")
    for artist in artists.json():
        artist_id = artist["artist_id"]
        albums = spotify_data.get_artist_albums(artist_id=artist_id)
        for album in albums["items"]:
            album_id = album.get("id", "")
            call_album(album_id=album_id, artist_id=artist_id)