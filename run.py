import requests

from dotenv import dotenv_values
config = dotenv_values(".env")

auth_url = 'https://accounts.spotify.com/api/token'
base_url = 'https://api.spotify.com/v1/'

# Get access token
def get_access_token():
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id' : config['CLIENT_ID'],
        'client_secret': config['CLIENT_SECRET']
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token
    
access_token = get_access_token()

# Get artist
def get_artist():
    pass

# Get related artists
def get_related_artists():
    pass

# Get artist top track
def get_artist_top_track():
    pass

