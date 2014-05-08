from bottle import route, request, run, view, template, static_file
from passlib.apps import custom_app_context as pwd_context
import pymongo
from pymongo import Connection
import datetime
import os

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/')
def login():
	return template('inicio')

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
		return template('inicio',nombre=username)

run(host='localhost', port=8070)

