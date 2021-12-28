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

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
# r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)


# Get related artists
def get_related_artists(artist_id):
    related_artists = requests.get(base_url + 'artists/' + artist_id + '/related-artists', headers=headers).json()
    related_artist_ids = [artist['id'] for artist in related_artists['artists']]
    return related_artist_ids

print(get_related_artists('1bwUhKRmEkOZ1wuTnV9XjC'))

# Get artist top track
def get_artist_top_track():
    pass

