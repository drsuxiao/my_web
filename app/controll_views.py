from flask_admin import expose, AdminIndexView, BaseView
from flask_admin import Admin, helpers
from app import app, db, login_manager
from app.data_models import User, Basefile, Amnioticrecord, Finehairrecord, Umbilicalbloodrecord, DateEncoder
from flask_login import current_user, login_user, logout_user
from app.view_forms import LoginForm, RegistrationForm, AmnioticForm, PasswordEditForm
from flask import render_template, redirect, url_for, request, flash, json, jsonify
from app.view_models import MyUserView, MyBasefileView, MyAmnioticrecordView, MyBaseView


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


# 决定身份验证可见
def is_accessible():
    return current_user.is_authenticated


# Flask views
@app.route('/')
def index():
    return render_template('index.html')

'''
@app.route('/admin/user/new/', methods=['GET', 'POST'])
def create_user():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate(form):
        return render_template('my_user_create.html', form=form)
    return render_template('my_user_create.html', form=form)
'''

# 每个自定义视图必须提供一个@expose(‘/‘) 的index方法,否则会报错
# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)
            print(form.data)
        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()
            print('自定义闯将')
            form.populate_obj(user)   # 把form直接转成orm的数据
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            # user.password = generate_password_hash(form.password.data)
            # admin 创建模板的密码是明文，需要重写
            db.session.add(user)
            db.session.commit()

            login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))

    @expose('/password/', methods=['GET', 'POST'])
    def password_edit(self):
        form = PasswordEditForm()
        if helpers.validate_form_on_submit(form):
            user = db.session.query(User).filter(User.id == current_user.id).first()
            old_password = form.old_password.data
            if user.password == old_password:
                user.password = form.password.data
                db.session.add(user)
                db.session.commit()
                flash('修改密码成功')
                return redirect(url_for('.index'))
            flash('原密码不正确')
        return self.render('/admin/my_password_edit.html', form=form)


class MyAppendView(MyBaseView):

    @expose('/', methods=['GET'])
    def index(self):
        form = AmnioticForm()
        #data = db.session.query(Amnioticrecord).filter(Amnioticrecord.id == id).first().to_json()
        return self.render('my_amniotic_append.html', form=form)

    @expose('/new/', methods=['GET', 'POST'])
    def amniotic_new(self):
        print(request.method)
        form = AmnioticForm(request.form)
        print(form.data)
        if request.method == 'POST':
            print('enter')
            amuiotic = Amnioticrecord()
            form.populate_obj(amuiotic)
            db.session.add(amuiotic)
            db.session.commit()
            return redirect(url_for('.index'))
        return self.render('my_amniotic_append.html', form=form)

    @expose('/test_get/', methods=['POST', 'GET'])
    def test_get(self):
        # 获取Get数据
        id = request.args.get('id')
        # 返回
        row = db.session.query(Amnioticrecord).filter(Amnioticrecord.id == id).first()

        print(row.to_json())
        return row.to_json()


#使用自己重写的 Home view 来重置了库中原本提供的Home view
#@param url ='/admin' 系统默认的，可以自己修改,设置的内容等同于
#admin = Blueprint('admin', __name__, url_prefix='/admin')
#即该模块下的所有url 地址都将使用 url 来作为前缀


admin = Admin(app, name=u'病历管理系统', index_view=MyAdminIndexView(), base_template='my_master.html')
# 添加页面

admin.add_view(MyUserView(User, db.session, name=u'用户管理', category='系统'))
admin.add_view(MyBasefileView(Basefile, db.session, name='基础档案表设置', category='系统'))

admin.add_view(MyAppendView(name=u'羊水录入', endpoint='amniotic', category='病历数据录入'))
admin.add_view(MyAppendView(name=u'绒毛录入', endpoint='fluff', category='病历数据录入'))
admin.add_view(MyAppendView(name=u'脐血录入', endpoint='cordblood', category='病历数据录入'))

admin.add_view(MyAmnioticrecordView(Amnioticrecord, db.session, name='羊水病历', category='病历数据查询'))
#admin.add_view(MyAmnioticrecordView(Finehairrecord, db.session, name='绒毛病历', category='病历数据查询'))
#admin.add_view(MyAmnioticrecordView(Umbilicalbloodrecord, db.session, name='脐血病历', category='病历数据查询'))


# admin.add_view(MyView(name=u'用户管理'))
# 添加下拉页面
#admin.add_view(MyView(name='Hello 1', endpoint='test1', category='Subview'))




