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

# Return artist ID
def get_artist_id():
    artist_id = '1bwUhKRmEkOZ1wuTnV9XjC'
    return artist_id

# Get related artists
def get_related_artists(artist_id):
    related_artists = requests.get(base_url + 'artists/' + artist_id + '/related-artists', headers=headers).json()
    related_artist_ids = [artist['id'] for artist in related_artists['artists']]
    return related_artist_ids

# print(get_related_artists(get_artist_id()))


# TODO get location of Spotify user for market parameter
# Get artist top track
def get_artist_top_track(artist_id):
    params = {'market': 'GB'}
    top_track = requests.get(base_url + 'artists/' + artist_id + '/top-tracks', params=params, headers=headers).json()
    return top_track

print(get_artist_top_track('6Nii4K84ZzBZS8X2MP8c9t'))

# Iterate through list of related artists and return top track of each
# TODO use asyncio or threading to return top tracks asynchronously
def get_all_top_tracks(related_artists):
    top_tracks = []
    return top_tracks



# Create playlist and return playlist ID
# TODO Authorization flow
def create_playlist():
    # /v1/users/user_id/playlists HTTP/1.1
    # new_playlist = requests.post(base_url + 'users/' + config['SPOTIFY_USER_ID'] + '/playlists', headers=headers
    # )   
    # return new_playlist.json()
    pass


def add_playlist_tracks(playlist_id):
    pass
