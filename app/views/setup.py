from flask import Flask
from flask_restplus import Api
authorizations = {'apikey':{
	'type':'apiKey',
	'in':'header',
	'name':'X-API-KEY'
}}
app = Flask(__name__)
api = Api(app,authorizations=authorizations)