import jwt

from flask import request
from functools import wraps

from .setup import app

def token_required(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		token = None
		if 'X-API-KEY' in request.headers:
			token = request.headers['X-API-KEY']
		if not token:
			return {'result':'token is missing'}
		try:
			jwt.decode(token,app.config['SECRET_KEY'],algorithm='HS256')
		except:
			return {'result':'token is invalid'}

	
		return f(*args,**kwargs)
	return decorated
