from app.views.setup import app
from app.views.views import *


app.config.from_pyfile('config.cfg')

if __name__ == '__main__':
	app.run()