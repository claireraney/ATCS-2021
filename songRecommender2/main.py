import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "3f626ffc7e274c8ea070c3d2bf8f2b32"
client_secret = "765381053a9f497eb2ad1ce0f4c0ec58"
scope = "user-library-read"
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri='http://127.0.0.1:9090', scope=scope))
# results = sp.search(q="artist:OneRepublic")
# print(results)
# print(results['tracks']['items'])
# # print(sp.search(q="artist:OneRepublic"))
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track)
#
# print(sp.album("3RBULTZJ97bvVzZLpxcB0j"))

import tekore as tk

app_token = tk.request_client_token(client_id, client_secret)

spotify = tk.Spotify(app_token)

album = spotify.album('3RBULTZJ97bvVzZLpxcB0j')
for track in album.tracks.items:
    print(track.track_number, track.name)