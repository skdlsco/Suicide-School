from flask import Response, Blueprint, request
from bson import json_util
from application.db import users
import uuid
auth = Blueprint('/auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    id = request.form['id']
    password = request.form['password']
    user = users.find_one({'id' : id})
    if not user:
        return failed()

    if user['password'] != password:
        return failed()

    return Response(response=json_util.dumps({'status' : True, 'data' : user}), status = 200, mimetype = 'application/json')

@auth.route('/register', methods=['POST'])
def register():
    username = request.form['name']
    password = request.form['password']
    id = request.form['id']
    token = str(uuid.uuid4()).replace('-','')

    if users.find_one({'name' : username}) or users.find_one({'id' : id}):
        return failed()

    user = json_util.dumps({'name' : username, 'password' : password, 'id' : id, 'token' : token})
    users.insert(json_util.loads(user))
    return Response(response=json_util.dumps({'status' : True, 'data' : json_util.loads(user)}), status = 200, mimetype = 'application/json')

@auth.route('/getData', methods=['GET'])
def getData():
    token = request.args['token']
    user = users.find_one({'token' : token})

    if not user:
        return failed()
    return Response(response=json_util.dumps({'status' : True, 'data' : user}), status = 200, mimetype = 'application/json' )
def failed():
    return Response(response=json_util.dumps({'status' : False}), status = 404, mimetype ='application/json')
