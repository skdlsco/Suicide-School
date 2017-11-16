from flask import Flask
from flask_cors import CORS
from application.auth import auth
from application.chapters import chapter

app = Flask(__name__)
app.secret_key = 'this is secret key'
CORS(app)
app.register_blueprint(auth, url_prefix = '/auth')
app.register_blueprint(chapter, url_prefix = '/chapter')

