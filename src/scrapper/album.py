"""
Artist: Relationship to Artist ID
ID
Album Metrics:
Title: 'name'
Music Label: 'label'
Popularity
Release Date
Total Tracks
Tracks: relationship to Track table ID
Type: (example: album)
"""
from src.scrapper.spotify_data import (SpotifyData, client_id, client_secret)
import json



spotify_data = SpotifyData(client_id=client_id, client_secret=client_secret)
album_tracks = spotify_data.get_album_data()
with open("album_tracks.json", "w") as file:
    json.dump(album_tracks["items"][0], file)
print("Done")


