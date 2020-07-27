from fuzzywuzzy import fuzz
import json
import spotipy
import auth


def get_correct_artist_from_results(results, target):
    for result in results:
        result_artist = result['name']
        match = fuzz.partial_ratio(target, result_artist)
        if match > 85:
            return result
    raise ValueError(f'{target} not found')


def get_correct_album_from_results(artist, target, sp):
    offsets = [0, 50, 100, 150, 200]
    artist_id = artist['id']
    for offset in offsets:
        results = sp.artist_albums(artist_id=artist_id, limit=50, offset=offset)['items']

        for result in results:
            result_album = result["name"]
            match = fuzz.partial_ratio(target, result_album)
            opp_match = fuzz.partial_ratio(result_album, target)
            # print(result_album, target, match)
            if (match > 85) or (opp_match > 85):
                print(result_album, target, match)
                print('\n\n')
                return result


def search_for_album(album, target_artist, target_album, sp):
    if "id" in album:
        return sp.album(album_id=album["id"])
    artists = sp.search(q=album["artist"],
                        type='artist',
                        limit=50)
    artists = artists['artists']['items']
    artist = get_correct_artist_from_results(artists, target_artist)
    album = get_correct_album_from_results(artist, target_album, sp)
    return album


def create_rsgaoat_playlist(albums, start, end, sp, user):
    playlist_name = f'Rolling Stone GAOAT {start}-{end}'
    playlist_id = sp.user_playlist_create(user['id'], playlist_name)['id']
    section_albums = [album for album in albums if album['position'] in range(start, end)][::-1]
    for album in section_albums:
        target_artist = album['artist']
        target_album = album['album']
        print(target_artist, target_album, album['position'])
        result = search_for_album(album, target_artist, target_album, sp)
        try:
            tracks = [track['id'] for track in sp.album_tracks(result['id'])['items']]
        except spotipy.exceptions.SpotifyException:
            tracks = [track['id'] for track in sp.playlist_tracks(result['id'])['items']]
        sp.user_playlist_add_tracks(user['id'], playlist_id, tracks)


if __name__ == "__main__":
    token = auth.get_new_access_token()
    sp = spotipy.Spotify(auth=token)
    user = sp.current_user()

    boundaries = [
        (475, 501),
        (450, 475),
        (425, 450),
        (400, 425),
        (375, 400),
        (350, 475),
        (325, 450),
        (300, 425),
        (275, 300),
        (250, 275),
        (225, 250),
        (200, 225),
        (175, 200),
        (150, 175),
        (125, 150),
        (100, 125),
        (75, 100),
        (50, 75),
        (25, 50),
        (0, 25),

    ]

    with open('rs_top_500.json') as f:
        albums = json.load(f)['data']
    for start, end in boundaries:
        create_rsgaoat_playlist(albums, start, end, sp, user)
