import errors
from domain import tracks


def get_all_tracks_on_playlist(playlist, sp):
    all_track_data = []
    result = sp.search(type='playlist', q=playlist)
    try:
        name_id = [(i['id'], i['name'], playlist) for i in result['playlists']['items']][0]
        sp_playlist = sp.playlist_tracks(playlist_id=name_id[0])
        track = [i['track'] for i in sp_playlist['items']]
        for i in track:
            track_data = tracks.extract_track_data(track=i, sp=sp)
            all_track_data.append(track_data)
    except IndexError:
        print(f'{playlist} not found')
    except errors.TrackError as e:
        print(e)
    except Exception as e:
        print(e)
    return all_track_data


if __name__ == "__main__":
    import json
    import spotipy
    import auth
    token = auth.get_new_access_token()

    sp = spotipy.Spotify(auth=token)

    extract = []
    with open('playlists.json') as f:
        data = json.load(f)

    for idx, playlist in data.items():
        print(f'{idx}/{len(data)}')
        extract.append(get_all_tracks_on_playlist(playlist, sp))
