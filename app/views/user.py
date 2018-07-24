import jwt

from flask import request
from flask_restplus import Resource

from .setup import api
from .auth import *

class Login(Resource):
	def post(self):
		token = jwt.encode({'email':'name'},app.config['SECRET_KEY'],algorithm='HS256')
		token=token.decode('UTF-8')
		return {'TOKEN':token}

class Protected(Resource):
	@token_required
	@api.doc(security='apikey')
	def get(self):
		name = jwt.decode(request.headers['X-API-KEY'],app.config['SECRET_KEY'],algorithm='HS256')
		return name