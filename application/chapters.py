from flask import Response, request, session, Blueprint, render_template, redirect,  make_response
from application.db import users
from bson import json_util
import datetime
import time

chapter = Blueprint('/chapter', __name__)

@chapter.route('/', methods=['GET'])
def chapters():
    chapter = request.args.get('ch', default=0)
    if chapter == "x":
        chapter = 11
    if(float(chapter) == 0):
        if 'token' in request.cookies:
            token  =  request.cookies.get('token')
            user = users.find_one({'token' : token})
            if  not user:
                return  redirect('/auth/login')
            uChapter =  user['chapter']

            if int(uChapter) == 0:
                return  render_template("ch0.html")
            return redirect("/chapter?"+"ch="+str(int(float(uChapter))))

        return render_template("ch0.html")
    if 'token' not in request.cookies:
        return redirect('/auth/login')
    token = request.cookies.get('token')
    user =  users.find_one({'token' : token})
    if not  user:
        return redirect('/auth/login')
    timer = user['timer']
    now = time.mktime(datetime.datetime.now().timetuple())
    if now > timer:
        now = datetime.datetime.now()
        if float(chapter) + 0.5 >= float(user['chapter']):
            print(user['chapter'], float(chapter))
            user['chapter'] = float(user['chapter']) + 0.5
            timer = time.mktime((now + datetime.timedelta(seconds=10)).timetuple())
            user['timer'] =  timer
            users.update({'token' : token}, user)
    uChapter = float(user['chapter'])
    if float(chapter) > uChapter:
        return redirect("/chapter?ch=" + str(int(uChapter)))
    template = "ch"+str(int(float(chapter)))+".html"
    if float(chapter) > 10:
        template = "chx.html"
    return render_template(template)

@chapter.route('/getAfter', methods=['POST'])
def getAfter():
    if 'token' not in request.cookies:
        return failed()
    ch = request.form['ch']
    token = request.cookies.get('token')
    user = users.find_one({'token' : token})
    if not user:
        return failed()
    timer = user['timer']
    now = time.mktime(datetime.datetime.now().timetuple())
    if now > timer:
        now = datetime.datetime.now()
        if float(ch) == float(user['chapter']):
            user['chapter'] = float(user['chapter'])+float(0.5)
            timer = time.mktime((now + datetime.timedelta(seconds=10)).timetuple())
            user['timer'] = timer
            users.update({'token' : token}, user)
        return Response(response=json_util.dumps({'status' : True}), mimetype = 'application/json')
    if float(ch) < float(user['chapter']):
        return Response(response=json_util.dumps({'status':True}),mimetype = 'application/json')
    return failed()

def failed():
    return Response(response=json_util.dumps({'status' : False}), mimetype = 'application/json')
