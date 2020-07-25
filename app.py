from flask import Flask
import os
import requests

app = Flask(__name__)

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')


@app.route('/')
def hello_world():
    url = f"https://accounts.spotify.com/authorize?client_id={client_id}4&response_type=code&redirect_uri={redirect_uri}"
    response = requests.get(url)
    print(response)
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True, port=8000)
