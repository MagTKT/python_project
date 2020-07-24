#!/usr/bin/env python3

from datetime import datetime

from socket import socket

from flask import Flask, request, render_template, \
                  redirect

from model_sqlite import save, \
                read, \
                getAll, \
                save_user,\
                getAll_users

app = Flask(__name__)

@app.route('/')
def index():
    #d = { 'last_added':[ { 'uid':'testuid', 'code':'testcode' } ] }
    d = { 'last_added':getAll() }
    return render_template('index.html',**d)

@app.route('/create')
def create():
    uid = save()
    return redirect("{}edit/{}".format(request.host_url,uid))
    
@app.route('/edit/<string:uid>/')
def edit(uid):
    info = read(uid)
    code = info['code']
    lang = info['lang']
    date_time = datetime.now()
    ip = request.remote_addr
    user_agent = str(request.user_agent)
    navigator = request.headers.get('User-Agent')

    user = save_user(ip, navigator, date_time)
    if code is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=code, lang = lang,
              url="{}view/{}".format(request.host_url,uid))
    return render_template('edit.html', **d) 

@app.route('/publish',methods=['POST'])
def publish():
    code = request.form['code']
    uid  = request.form['uid']
    lang = request.form['lang']
    save(uid,code,lang)
    return redirect("{}{}/{}".format(request.host_url,
                                     request.form['submit'],
                                     uid))

@app.route('/view/<string:uid>/')
def view(uid):
    info = read(uid)
    code = info['code']
    lang = info['lang']
    if code is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=code, lang=lang,
              url="{}view/{}".format(request.host_url,uid))
    return render_template('view.html', **d)

@app.route('/admin/')
def admin():
    d = { 'last_added': getAll_users() }
    return render_template('admin.html', **d)

if __name__ == '__main__':
    app.run()