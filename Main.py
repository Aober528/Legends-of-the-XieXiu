from flask import Flask
from app.views import game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LXX'

app.register_blueprint(game, url_prefix='/')

if __name__ == '__main__':
	app.run(debug=True, port=80)