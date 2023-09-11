# import requests

# # Replace 'mbid' with the actual MusicBrainz artist ID
# artist_mbid = '65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab'

# # Make the API request
# url = f'https://musicbrainz.org/ws/2/artist/{artist_mbid}?fmt=json'
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     artist_data = response.json()
#     print(artist_data)
#     # Process the JSON data as needed
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace with your actual credentials
client_id = 'f4d03d2f65594e10900a7de11b57c68b'
client_secret = 'cbf6500d4009478184f8961d5b731605'

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Fetch and print music data
def fetch_and_print_music_data():
    # Example: Search for tracks with a specific keyword (e.g., "rock")
    results = sp.search(q='rock', type='track', limit=10)

    # Extract and print details for each track
    for track in results['tracks']['items']:
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        album_name = track['album']['name']
        print(f"Track: {track_name}")
        print(f"Artist: {artist_name}")
        print(f"Album: {album_name}")
        print("-" * 40)

if __name__ == "__main__":
    fetch_and_print_music_data()
