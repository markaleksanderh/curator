from flask import Flask, render_template
from flask_cors import CORS
import requests
import os

# from dotenv import dotenv_values
# config = dotenv_values(".env")

auth_url = 'https://accounts.spotify.com/api/token'

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/authenticate')
    def get_access_token():
        auth_response = requests.post(auth_url, {
            'grant_type': 'client_credentials',
            'client_id' : os.environ['CLIENT_ID'],
            'client_secret': os.environ['CLIENT_SECRET']            
        })
        auth_response_data = auth_response.json()
        access_token = auth_response_data['access_token']
        return access_token

    @app.errorhandler(404)
    def page_not_found(error):
        return "404 Page not found"

    return app