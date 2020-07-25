import pandas as pd
import json

song_info = pd.read_csv('/Users/jackbicknell/ga/ds-bootcamp/data/song_info.csv')

playlists = song_info['playlist'].unique()
playlists = {idx: i for idx, i in enumerate(playlists)}


with open('playlists.json', 'w') as fp:
    json.dump(playlists, fp)
