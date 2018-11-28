from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app.data_models import User
from flask_admin import BaseView


class MyBaseView(BaseView):
    """ 模型视图基类 """
    def is_accessible(self):
        return current_user.is_authenticated


class BaseModelView(ModelView):
    """ 模型视图基类 """
    def is_accessible(self):
        return current_user.is_authenticated
    page_size = 10  # 每页显示几条
    column_display_pk = True   #在页面中是否显示主键
    can_create = True   # 可以创建数据  False
    can_view_details = True   # 可以查看详情  False
    can_export = True
    details_modal = False    # 查看详细时是否弹出对话框
    edit_modal = False  #  编辑时是否弹出对话框

    #设置每个列的显示数据的格式化
    # column_formatters = {}
    # 不要完全覆盖内置的模板，最好是扩展它们。 这将使您更容易升级到新的Flask - Admin版本
    # edit_template = 'my_edit.html'
    # create_template = 'my_create.html'
    # list_template = 'my_list.html'


class MyUserView(BaseModelView):
    """具体的模型视图"""
    can_export = False  # 可以创建数据  False
    column_searchable_list = ['id', 'username', 'login', 'create_time']   # 可以搜索的列名
    column_filters = column_searchable_list
    column_list = ['id', 'username', 'login', 'create_time']   # 填入想要显示的字段，不填的话自动从模型中取
    #column_exclude_list    填入不想显示的字段
    column_editable_list = ['username', 'password', 'login']    # 可以被编辑的字段
    column_labels = {
        'id': u'编号',
        'username': u'用户名',
        'password': u'密码',
        'login': u'登录账号',
        'create_time': u'创建时间'
    }
    form_args = {'username': {'render_kw': {"multiple": "multiple"}}}
    form_choices = {'username': [(n.username, n.username) for n in User.query.all()]}
    create_template = 'my_user_create.html'


class MyBasefileView(BaseModelView):
    """具体的模型视图"""
    column_searchable_list = ['id',
                              'type_name',
                              'plan_code',
                              'field_name',
                              'basefile_name'
                              ]
    column_filters = column_searchable_list
    column_list = ['id',
                              'type_name',
                              'plan_code',
                              'field_name',
                              'basefile_name',
                              'colid',
                              'print_value',
                              'default_value',
                              'list_order',
                              'sort_type',
                              'sort_order',
                              'show_width',
                              'ifvisibled']   # 填入想要显示的字段，不填的话自动从模型中取
    #column_exclude_list    填入不想显示的字段
    column_editable_list = ['print_value',
                              'default_value',
                              'list_order',
                              'sort_type',
                              'sort_order',
                              'show_width',
                              'ifvisibled']    # 可以被编辑的字段
    column_labels = {
        'id': u'编号',
        'type_name': u'病历类型',
        'plan_code': u'方案编码',
        'field_name': u'字段名',
        'basefile_name': u'对应档案表',
        'colid': u'colid',
        'print_value': u'打印值',
        'default_value': u'默认录入值',
        'list_order': u'列表顺序',
        'sort_type': u'排序方式',
        'sort_order': u'排序顺序',
        'show_width': u'显示宽度',
        'ifvisibled': u'是否显示'
    }


class MyAmnioticrecordView(BaseModelView):
    """具体的模型视图"""
    can_export = True  # 可以创建数据  False
    create_template = 'my_amniotic_create.html'
    column_labels = {'id': u'编号', 'records': u'病历册'}