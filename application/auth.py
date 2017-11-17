from flask import Response, Blueprint, request, session, render_template, redirect, make_response, url_for
from bson import json_util
from application.db import users
import datetime
import time
import uuid
auth = Blueprint('/auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if 'token' in  request.cookies:
            token = request.cookies.get('token')
            user = users.find_one({'token' : token})
            if user:
                return redirect('/chapter')
        return render_template('login.html')

    id = request.form['id']
    password = request.form['password']
    user = users.find_one({'id' : id})
    if not user:
        return failed()

    if user['password'] != password:
        return failed()

    res = Response(response=json_util.dumps({'status' : True, 'data' : user}), status = 200, mimetype = 'application/json')
    resp = make_response(res)
    if 'remember' in request.form:
        date_expire =  datetime.datetime.now()
        date_expire = date_expire + datetime.timedelta(days=31)
        resp.set_cookie('token', user['token'], expires=date_expire)
    else:
        resp.set_cookie('token', user['token'])
    return res

@auth.route('/signup', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('signup.html')

    password = request.form['password']
    id = request.form['id']
    token = str(uuid.uuid4()).replace('-','')
    chapter  =  1
    timer = time.mktime((datetime.datetime.now() + datetime.timedelta(seconds=10)).timetuple())
    if users.find_one({'id' : id}):
        return failed()

    user = json_util.dumps({'password' : password, 'id' : id, 'token' : token, 'chapter' : chapter, 'timer' : timer})
    users.insert(json_util.loads(user))
    return Response(response=json_util.dumps({'status' : True}), status = 200, mimetype = 'application/json')

@auth.route('/getData', methods=['GET'])
def getData():
    token = request.cookies.get('token')
    user = users.find_one({'token' : token})

    if not user:
        return failed()
    return Response(response=json_util.dumps({'status' : True, 'data' : user}), status = 200, mimetype = 'application/json' )
def failed():
    return Response(response=json_util.dumps({'status' : False}), status = 200, mimetype ='application/json')
