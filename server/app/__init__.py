from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return "Curator API"

    @app.errorhandler(404)
    def page_not_found(error):
        return "404 Page not found"

    return app