from app import app, db
from app.data_models import User
'''
db.drop_all()
db.create_all()

user1 = User(login='001', username='admin', password='123')
user2 = User(login='002', username='user', password='123')
db.session.add(user1)
db.session.add(user2)
db.session.commit()
'''

if __name__ == '__main__':
    app.run(host="138.62.99.248", port=5050, debug=True)
