from flask import Flask
from flask_cors import CORS
from application.auth import auth


app = Flask(__name__)
app.secret_key = 'this is secret key'
CORS(app)
app.register_blueprint(auth, url_prefix = '/auth')

