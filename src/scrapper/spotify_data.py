import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from decouple import config
import json

client_id = config("CLIENT_ID")
client_secret = config("CLIENT_SECRET")


client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class SpotifyData:
    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(
                client_id=client_id, client_secret=client_secret
            )
        )

    def get_album_id(self, album):
        try:
            album_id = album.get("id", None)
            return album_id
        except Exception as e:
            print(e)

    def get_track_detail(self, track_id):
        track_info = self.sp.track(track_id)
        return track_info

    def get_artist_detail(self, artist_id):
        artist_info = self.sp.artist(artist_id)
        return artist_info

    def get_album_data(self):
        album_info = self.sp.album_tracks("5qmZefgh78fN3jsyPPlvuw")
        return album_info
