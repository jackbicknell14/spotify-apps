import pprint
import spotipy
import auth

if __name__ == "__main__":
    pp = pprint.PrettyPrinter()
    sp = spotipy.Spotify(auth=auth.get_new_access_token())
    user = sp.current_user()
    top_tracks = sp.current_user_top_tracks(time_range='short_term', limit=10)['items']
    # tracks = [i['id'] for i in top_tracks]
    tracks = [i['name'] for i in top_tracks]
    print(tracks)
    # playlist_name = f'JULY 20'
    # playlist_id = sp.user_playlist_create(user['id'], playlist_name)['id']
    # sp.user_playlist_add_tracks(user['id'], playlist_id, tracks)
