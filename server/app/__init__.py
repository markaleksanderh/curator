from flask import (
    Flask,
    render_template,
    make_response,
    redirect
)

from flask_cors import CORS
import requests
import os
from urllib.parse import urlencode

auth_url = 'https://accounts.spotify.com/api/token'

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        payload = {
            'client_id': os.environ['CLIENT_ID'],
            'response_type': 'code',
            'redirect_uri': os.environ['REDIRECT_URI'],
            'scope': 'user-read-private user-read-email',
        }
        res = make_response(redirect('{}/?{}'.format(auth_url, urlencode(payload))))
        return res

    def logout():
        pass

    @app.route('/callback')
    def callback():
        pass

    @app.route('/refresh_token')
    def refresh_token():
        pass    

    @app.errorhandler(404)
    def page_not_found(error):
        return "404 Page not found"

    return app