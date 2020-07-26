import pprint
import spotipy
import json
import auth
from use_case import playlist as pl
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

token = auth.get_new_access_token()
pp = pprint.PrettyPrinter()
sp = spotipy.Spotify(auth=token)
user = sp.current_user()
top_tracks = sp.current_user_top_tracks(time_range='short_term', limit=10)['items']
tracks = [i['name'] for i in top_tracks]
# playlist_name = f'JULY 20'
# playlist_id = sp.user_playlist_create(user['id'], playlist_name)['id']
# sp.user_playlist_add_tracks(user['id'], playlist_id, tracks)
print(tracks)
