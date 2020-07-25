import requests
import config


def get_new_access_token():
    url = 'https://accounts.spotify.com/api/token'
    body = {
        'grant_type': 'refresh_token',
        'refresh_token': config.REFRESH_TOKEN,
        'client_id': config.CLIENT_ID,
        'client_secret': config.CLIENT_SECRET
    }
    response = requests.post(url=url, data=body)
    data = response.json()
    return data['access_token']
