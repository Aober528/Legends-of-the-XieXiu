from flask import Blueprint, render_template, redirect, url_for
import app.forms as forms
import sqlite3
import json

game = Blueprint('game', __name__)

@game.route('/', methods=['GET', 'POST'])
def index():
	conn = sqlite3.connect('.\\data\\lxx.db')
	cursor = conn.cursor()
	cursor.execute('select * from user where 1 = 1')
	if len(cursor.fetchall()) == 4:
		return redirect(url_for('game.fall'))
	else:
		form = forms.RegisterForm()
		data = {}
		if form.validate_on_submit():
			username = form.username.data
			password = form.password.data

			cursor.execute('select * from user where name = ?', (username,))
			if cursor.fetchall() != []:
				form.username.errors = ['用户名已被占用']
				cursor.close()
				conn.commit()
				conn.close()
			else:
				with open('.\\data\\config.json', 'r', encoding='utf-8') as config:
					data = json.load(config)
				if password != data['password']:
					form.password.errors = ['密钥错误']
				else:
					cursor.execute('insert into user (name) values(?)', (username,))
					cursor.close()
					conn.commit()
					conn.close()
					return redirect(url_for('game.main'))
	return render_template('index.html', form = form)

@game.route('/fall')
def fall():
	return render_template('fall.html')

@game.route('/main', methods=['GET', 'POST'])
def main():
	return 'game'