from .setup import api
from .user import Login, Protected

api.add_resource(Login,'/login')
api.add_resource(Protected,'/protected')