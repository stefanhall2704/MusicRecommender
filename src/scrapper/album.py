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
    json_data = {
        "title": title,
        "duration_ms": duration_ms,
        "explicit": explicit,
        "track_id": track_id,
        "spotify_url": spotify_url,
        "album_id": album_id,
        "artist_id": artist_id
    }
    requests.post("http://localhost:4000/api/track/create", json=json_data)
    


def tracks(album_id: int, artist_id: int) -> None:
    album_tracks = spotify_data.get_album_tracks(album_id=album_id)
    tracks = album_tracks["items"]
    for track in tracks:
        call_track(track=track, album_id=album_id, artist_id=artist_id)
        

def call_album(album_id: int, artist_id: int):
    album_data = spotify_data.get_album_data(album_id=album_id)
    title = album_data["name"]
    music_label = album_data["label"]
    popularity = album_data["popularity"]
    release_date = album_data["release_date"]
    total_tracks = album_data["total_tracks"]
    type = album_data["type"]
    json_data = {
        "title": title,
        "music_label": music_label,
        "popularity": popularity,
        "release_date": release_date,
        "total_tracks": total_tracks,
        "type": type,
        "album_id": album_id,
        "artist_id": artist_id
    }
    response = requests.post("http://localhost:4000/api/album/create", json=json_data)
    print(response.status_code)
    tracks(album_id=album_id, artist_id=artist_id)


if __name__ == "__main__":
    """
    Due to ID offset of 2, start skip at current running total - 2.
    Scrapes:
    Scrape 1: 9/18/2023 total: 169
    Scrape 2: 
    """
    artists = requests.get("http://localhost:4000/api/artist/limited_artists?limit=9831&skip=167")
    for artist in artists.json():
        artist_id = artist["artist_id"]
        print({"artist": artist["name"], "ID": artist["ID"]})
        albums = spotify_data.get_artist_albums(artist_id=artist_id)
        for album in albums["items"]:
            album_id = album.get("id", "")
            call_album(album_id=album_id, artist_id=artist_id)