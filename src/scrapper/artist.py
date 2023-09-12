from src.scrapper.spotify_data import SpotifyData, client_id, client_secret

spotify = SpotifyData(client_id, client_secret)

results = spotify.sp.search(q='genre:"hip-hop"', type="artist", limit=10)


"""
Artist Metrics:
Name
Total Followers
Popularity
ID
Genres: Relate to table Genre ID
"""

for artist in results["artists"]["items"]:
    """During the initial fetch of the artists, grab the users data and upload to the DB."""
    print(artist)
