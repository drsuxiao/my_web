from app.models import User, Role, Basefile
from app import db
from sqlalchemy import desc
from datetime import datetime


def get_next_uid(model):
    m = db.session.query(model).order_by(model.id.desc).first()

    return m.id + 1


def user_new(user_dict):
    if len(user_dict) == 0:
        return 0
    user = User()
    #user.id = get_next_uid
    user.code = user_dict.get('name')
    user.name = user_dict.get('code')
    user.password = user_dict.get('password', "123")
    user.create_time = user_dict.get('create_time', datetime.now())
    user.role_id = user_dict.get('role_id', 0)
    db.session.add(user)
    db.session.commit()

    return 1


def user_edit(key, user_dict):
    user = db.session.query.filter(User.id == key).first()
    if user:
        user.code = user_dict.get('name')
        user.name = user_dict.get('code')
        user.password = user_dict.get('password', "123")
        db.session.commit()

    for key, value in user_dict.items:
        if key not in ['id']:
            user[key] = value

    return 1


def user_delete(key):
    user = db.session.query(User).filter(User.id == key).first()
    db.session.delete(user)
    db.session.commit()

    return 0


def get_user_bykey(key):
    user = db.session.query(User).filter(User.id == key).first()

    return user.to_dict()


def get_users():
    users = db.session.query(User).all()
    list = []
    for u in users:
        list.append(u.to_dict())

    return list


