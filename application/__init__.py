from flask import Flask
from application.auth import auth

app = Flask(__name__)
app.register_blueprint(auth, url_prefix = '/auth')

