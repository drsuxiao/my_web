from flask_script import Manager
from app import app, db
from flask_migrate import Migrate, MigrateCommand


manager = Manager(app)
# init  migrate upgrade
# 模型 -> 迁移文件 -> 表
# 1.要使用flask_migrate,必须绑定app和DB
migrate = Migrate(app, db)

# 2.把migrateCommand命令添加到manager中。
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


'''
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
'''
