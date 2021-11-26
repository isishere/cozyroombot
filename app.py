from flask import Flask, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import waitress

import config

app = Flask(__name__)


app.secret_key = ""
app.config['SESSION_COOKIE_NAME'] = 'Ilya Cookie'


@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host='0.0.0.0', port=8000)


@app.route('/redirect')
def redirectPage():
    return 'redirecting...'


@app.route('/getTracks')
def getTracks():
    return 'Some songs'


def create_spotify_oauth():
    return SpotifyOAuth(client_id=f'{config.CLIENT_ID}',
                        client_secret=f'{config.CLIENT_SECRET}',
                        redirect_uri=url_for('redirectPage', _external=True),
                        scope='user-library-read')
