from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel
from flask_login import LoginManager
from flask_bootstrap3 import Bootstrap

app = Flask(__name__)

# 汉化flask—admin
babel = Babel(app)

app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

bootstrap = Bootstrap(app)

from app import controll_views


