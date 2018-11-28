import os


basedir = os.path.abspath(os.path.dirname(__file__))  #项目的根目录
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
print(SQLALCHEMY_DATABASE_URI)

BABEL_DEFAULT_LOCALE = 'zh_CN'

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
