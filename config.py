import os


basedir = os.path.abspath(os.path.dirname(__file__))  #项目的根目录
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')   # 是文件夹，我们将会把 SQLAlchemy-migrate 数据文件存储在这里。
print(SQLALCHEMY_DATABASE_URI)
print(SQLALCHEMY_MIGRATE_REPO)

BABEL_DEFAULT_LOCALE = 'zh_CN'

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

FLASK_ADMIN_FLUID_LAYOUT = True