from flask import (
    Flask,
    render_template,
    make_response,
    redirect,
    request,
    session,
    url_for,
    jsonify,
)

import string
import random

from flask_cors import CORS
import requests
import os
from urllib.parse import urlencode

auth_url = 'https://accounts.spotify.com/authorize'
token_url = 'https://accounts.spotify.com/api/token'
profile_url = 'https://api.spotify.com/v1/me'
search_url = 'https://api.spotify.com/v1/search'

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ['SECRET_KEY']
    CORS(app)

    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/login', methods=['GET'])
    def login():
        state = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(16))
        scope = 'user-read-private user-read-email'
        payload = {
            'client_id': os.environ['CLIENT_ID'],
            'response_type': 'code',
            'redirect_uri': 'http://localhost:5000/callback',
            'state': state,
            'scope': scope,
        }
        res = make_response(redirect('{}/?{}'.format(auth_url, urlencode(payload))))
        res.set_cookie('spotify_auth_state', state)
        return res

    @app.route('/logout')
    def logout():
        state = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(16))
        scope = 'user-read-private user-read-email'
        payload = {
            'client_id': os.environ['CLIENT_ID'],
            'response_type': 'code',
            'redirect_uri': 'http://localhost:5000/callback',
            'state': state,
            'scope': scope,
            'show_dialog': True,
        }
        res = make_response(redirect('{}/?{}'.format(auth_url, urlencode(payload))))
        res.set_cookie('spotify_auth_state', state)
        return res

    @app.route('/callback')
    def callback():
        error = request.args.get('error')
        code = request.args.get('code')
        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            # 'redirect_uri': os.environ['REDIRECT_URI'],
            'redirect_uri': 'http://localhost:5000/callback',
        }
        res = requests.post(token_url, auth=(os.environ['CLIENT_ID'], os.environ['CLIENT_SECRET']), data=payload)
        res_data = res.json()
        session['tokens'] = {
            'access_token': res_data.get('access_token'),
            'refresh_token': res_data.get('refresh_token'),
        }

        return redirect(url_for('profile'))  

    @app.route('/refresh_token')
    def refresh_token():
        pass

    @app.route('/profile')
    def profile():
        headers = {'Authorization': "Bearer {}".format(session['tokens'].get('access_token'))}
        res = requests.get(profile_url, headers=headers).json()
        return render_template('profile.html', data=res, tokens=session.get('tokens'))

    @app.route('/search')
    def search():
        # headers = {'Authorization': "Bearer {}".format(session['tokens'].get('access_token'))}
        pass

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({"message": "404 Page not found"})

    return app