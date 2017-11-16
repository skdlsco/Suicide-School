from flask import Blueprint, Response, request, session, render_template, redirect
from application.db import users

main = Blueprint('/', __name__)

@main.route('/', methods=['GET', 'POST'])
def main():
    return "this  is  main:"
