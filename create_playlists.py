# print(user)
# print(user['id'])
# print(user.keys())
rollingstongtop100_id = '3bmMXcGPbuUhO0CsuslAgj'
# sp.user_playlist_add_tracks(user=user['id'], playlist_id)

with open('rs_top_500.json') as f:
    data = json.load(f)


def get_album_from_results(album_results, album_query, artist):
    for album_result in album_results:

        album_artists = set(album_artist['name'].casefold() for album_artist in album_result['artists'])
        matching_album = album_result['name'].casefold() == album_query
        matching_artist = artist in album_artists
        breakpoint()
        # TODO: Ampersands
        if matching_artist:
            print(album_artists, artist)
        if matching_album and matching_artist:
            print(f'found album', album['name'], album['id'])
            return [track['id'] for track in sp.album_tracks(album['id'])['items']]

# playlist_name = 'RS-500-475'
# sp.user_playlist_create(user['id'], playlist_name)
# playlists = sp.user_playlists(user['id'])['items']
# for playlist in playlists:
#     if playlist['name'] == playlist_name:
#         playlist_id = playlist['id']

albums = data['data']
for album in albums:
    if album['position'] in range(475, 500):
        album_query = album['album'].casefold()
        artist = album['artist'].casefold()
        album_results = sp.search(q=album_query, type='album')['albums']['items']
        tracks = get_album_from_results(album_results, album_query, artist)
        if tracks is None:
            print(f"Couldn't find album for {artist} and {album_query}")
        # else:
        #     sp.user_playlist_add_tracks(user['id'], playlist_id, tracks)
