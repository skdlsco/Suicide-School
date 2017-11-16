from flask import Response, request, session, Blueprint, render_template, redirect,  make_response
from application.db import users
import datetime
import time

chapter = Blueprint('/chapter', __name__)

@chapter.route('/', methods=['GET'])
def chapters():

    if 'token' not in request.cookies:
        return redirect('/auth/login')
    chapter = request.args.get('ch', default=0)
    token = request.cookies.get('token')
    user =  users.find_one({'token' : token})
    print(type(user))
    if not  user:
        return redirect('/auth/login')
    timer = user['timer']
    now = time.mktime(datetime.datetime.now().timetuple())
    if now > timer:
        now = datetime.datetime.now()
        if int(chapter) > int(user['chapter']):
            user['chapter'] = user['chapter'] + 1
            timer = time.mktime((now + datetime.timedelta(seconds=10)).timetuple())
            user['timer'] =  timer
            users.update({'token' : token}, user)
    uChapter = int(user['chapter'])
    if chapter == "x":
        chapter = 11

    if int(chapter) > uChapter:
        return redirect("/chapter?ch=" + str(uChapter))
    if int(chapter) > 10:
        chapter = "x"
    template = "ch"+str(chapter)+".html"
    return render_template(template)
