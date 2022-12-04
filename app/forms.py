from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
	username = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
	password = PasswordField(label='密　钥', validators=[DataRequired('密钥不能为空')])
	submit = SubmitField(label='进入')