import errors


def extract_track_data(track, sp):
    if track is None:
        raise errors.TrackError(f"Could not find data for track")
    name = track['name']
    artist = track['artists'][0]['name']
    track_id = track['id']
    popularity = track['popularity']
    album = track['album']['name']
    explicit = track['explicit']
    duration = track['duration_ms']

    track_analysis = sp.audio_features(id)[0]
    track_data = {
        'name': name,
        'artist': artist,
        'id': track_id,
        'popularity': popularity,
        'album': album,
        'explicit': explicit,
        'duration': duration,
        'danceability': track_analysis['danceability'],
        'energy': track_analysis['energy'],
        'loudness': track_analysis['key'],
        'mode': track_analysis['mode'],
        'speechiness': track_analysis['speechiness'],
        'acousticness': track_analysis['acousticness'],
        'instrumentalness': track_analysis['instrumentalness'],
        'liveness': track_analysis['liveness'],
        'valence': track_analysis['valence'],
        'tempo': track_analysis['tempo'],
        'time_signature': track_analysis['time_signature']
    }
    return track_data
