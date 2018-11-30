#这里的fields和validators是用的Flask-WTForm
from wtforms import fields, validators
from flask_wtf import FlaskForm
from app import db
from app.data_models import User
from werkzeug.security import generate_password_hash, check_password_hash


# Define login and registration forms (for flask-login)
class LoginForm(FlaskForm):
    login = fields.StringField(label='登录账号', validators=[validators.required()])
    password = fields.PasswordField(label='密码', validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        # if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(FlaskForm):
    login = fields.StringField(label='登录账号', validators=[validators.required()])
    email = fields.StringField(label='邮箱')
    password = fields.PasswordField(label='密码', validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')
