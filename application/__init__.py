from flask import Flask, redirect
from flask_cors import CORS
from application.auth import auth
from application.chapters import chapter
from application.main import main_blueprint

app = Flask(__name__)
app.secret_key = 'this is secret key'
CORS(app)
app.register_blueprint(auth, url_prefix = '/auth')
app.register_blueprint(chapter, url_prefix = '/chapter')
app.register_blueprint(main_blueprint, url_prefix = '/main')

@app.errorhandler(404)
def page_not_found(self):
    print("asdfsdf")
    return redirect('/main')
