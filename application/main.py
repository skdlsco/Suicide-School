from flask import Blueprint, Response, request, session, render_template, redirect
from application.db import users

main_blueprint = Blueprint('/main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
