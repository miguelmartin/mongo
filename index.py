from bottle import route, request, run, view, template
from passlib.apps import custom_app_context as pwd_context
import pymongo
from pymongo import Connection
import datetime
import os


@route('/')
def login():
    return '''
        <form action="/gestion_usuarios" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password"/>
            <input value="Login" type="submit" />
        </form>
    '''

@route('/gestion_usuarios', method='POST')
@view('form_template')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    hash = '$6$rounds=42278$ZbbYfgk1TSSeHS96$KVLiVfN9Zq02lEdqbwVDyosijXj0o72C/VPMOneIYpzD4lt.PjOo7HRS3s442UjeNX/3T.f/5T1TJOcXSyyR.1'
    ok = pwd_context.verify(password, hash)
    if username == "admin" and ok == True:
		return template('template') 
    else:
		return "Necesita ser adminitrador para acceder"

run(host='localhost', port=8020)

