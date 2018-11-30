from app import app, db
from app.data_models import User


#db.drop_all()
#db.create_all()
'''
user = User(login='003', username='admin', password='123')
db.session.add(user)
db.session.commit()'''
if __name__ == '__main__':
    app.run(debug=True)
