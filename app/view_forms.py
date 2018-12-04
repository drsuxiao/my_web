#这里的fields和validators是用的Flask-WTForm
from wtforms import fields, validators, form
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
    username = fields.StringField(label='用户名', validators=[validators.DataRequired("请输入用户名！")])
    password = fields.PasswordField(label='密码', validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('登陆账号冲突')


class PasswordEditForm(FlaskForm):
    old_password = fields.PasswordField('原密码', validators=[validators.DataRequired()])
    password = fields.PasswordField('新密码', validators=[
        validators.DataRequired(), validators.EqualTo('password2', message='两次密码不一致')])
    # 表单中完成密码与确认密码一致性的验证
    password2 = fields.PasswordField('确认密码', validators=[validators.DataRequired()])
    submit = fields.SubmitField('更新密码')
    

class AmnioticForm(FlaskForm):
    id = fields.IntegerField(label='ID') #db.Column(db.Integer, primary_key=True)
    records = fields.StringField(label='病历册', validators=[validators.DataRequired()])#db.Column(db.String(30), nullable=False)
    record_no = fields.StringField(label='病历号', validators=[validators.DataRequired()]) #db.Column(db.String(20), nullable=False)
    sort_no = fields.IntegerField(label='排序号')#db.Column(db.Integer)
    wife_name = fields.StringField(label='孕妇', validators=[validators.DataRequired()])#db.Column(db.String(30), nullable=False)
    wife_age = fields.IntegerField()#db.Column(db.Integer, nullable=False)
    wife_birthday_year = fields.IntegerField()#db.Column(db.Integer, nullable=False)
    wife_birthday_month = fields.IntegerField()#db.Column(db.Integer, nullable=False)
    wife_origin = fields.StringField()#db.Column(db.String(30))
    wife_nation = fields.StringField()#db.Column(db.String(20))
    wife_profession = fields.StringField()#db.Column(db.String(30))
    wife_phone = fields.StringField()#db.Column(db.String(30))
    husband_name = fields.StringField()#db.Column(db.String(30))
    husband_age = fields.IntegerField()#db.Column(db.Integer)
    husband_birthday_year = fields.IntegerField()#db.Column(db.Integer)
    husband_birthday_month = fields.IntegerField()#db.Column(db.Integer)
    husband_origin = fields.StringField()#db.Column(db.String(30))
    husband_nation = fields.StringField()#db.Column(db.String(20))
    husband_profession = fields.StringField()#db.Column(db.String(30))
    husband_phone = fields.StringField()#db.Column(db.String(30))
    communication_address = fields.StringField()#db.Column(db.String(60))
    residential_telephone = fields.StringField()#db.Column(db.String(30))  # 住宅电话
    ifpoverty = fields.BooleanField()#db.Column(db.Boolean)   #双方地贫
    referral_status = fields.BooleanField()#db.Column(db.Boolean)   #是否转诊
    referral_hospital = fields.StringField()#db.Column(db.String(60))
    screen_date = fields.DateField()#db.Column(db.Date)   # 筛查日期
    pregnancy_week = fields.IntegerField()#db.Column(db.Integer)  # 孕周
    pregnancy_day = fields.IntegerField()#db.Column(db.Integer)
    afp_od = fields.FloatField()#db.Column(db.Float)
    afp_mo = fields.FloatField()#db.Column(db.Float)
    b_hcg_od = fields.FloatField()#db.Column(db.Float)
    b_hcg_mo = fields.FloatField()#db.Column(db.Float)
    tribody_risk_21 = fields.FloatField()#db.Column(db.Float)
    tribody_risk_18 = fields.FloatField()#db.Column(db.Float)
    tribody_risk_13 = fields.FloatField()#db.Column(db.Float)
    ontd_risk = fields.StringField()#db.Column(db.String(8))
    pappa_miu_ml = fields.FloatField()#db.Column(db.Float)
    pappa_mo = fields.FloatField()#db.Column(db.Float)
    check_date = fields.DateField()#db.Column(db.Date)
    check_hospital = fields.StringField()#db.Column(db.String(60))
    gene_detection_poverty = fields.StringField()#db.Column(db.String(50))    # 地贫基因检测
    red_crispy = fields.StringField()#db.Column(db.String(8))   #红脆
    wbc = fields.FloatField()#db.Column(db.Float)
    mcv = fields.FloatField()#db.Column(db.Float)
    mch = fields.FloatField()#db.Column(db.Float)
    hb = fields.FloatField()#db.Column(db.Float)
    bg = fields.FloatField()#db.Column(db.Float)
    rh = fields.StringField()#db.Column(db.String(20))
    hb_elect_a2 = fields.FloatField()#db.Column(db.Float)
    hb_elect_other = fields.StringField()#db.Column(db.String(20))
    husband_check_date = fields.DateField()#db.Column(db.Date)
    husband_check_hospital =fields.StringField()# db.Column(db.String(60))
    husband_gene_detection_poverty = fields.StringField()#db.Column(db.String(50))    # 地贫基因检测
    husband_red_crispy = fields.StringField()#db.Column(db.String(8))   #红脆
    husband_wbc = fields.FloatField()#db.Column(db.Float)
    husband_mcv = fields.FloatField()#db.Column(db.Float)
    husband_mch = fields.FloatField()#db.Column(db.Float)
    husband_hb = fields.FloatField()#db.Column(db.Float)
    husband_bg = fields.FloatField()#db.Column(db.Float)
    husband_rh = fields.StringField()#db.Column(db.String(20))
    husband_hb_elect_a2 = fields.FloatField()#db.Column(db.Float)
    husband_hb_elect_other = fields.StringField()#db.Column(db.String(20))
    b_check_date = fields.DateField()#db.Column(db.Date)   # B超日期
    b_check_hospital = fields.StringField()#db.Column(db.String(60))
    menolipsis_week = fields.IntegerField()#db.Column(db.Integer)  # 停经_周
    menolipsis_day = fields.IntegerField()#db.Column(db.Integer)  # 停经_天
    b_pregnancy_week = fields.IntegerField()# db.Column(db.Integer)  # B超孕周_周
    b_pregnancy_day = fields.IntegerField()#db.Column(db.Integer)
    bpd = fields.FloatField()#db.Column(db.Float)
    head_circumference = fields.FloatField()#db.Column(db.Float)  # 头围
    ventral_circumference = fields.FloatField()#db.Column(db.Float)   # 腹围
    ventral_diameter = fields.FloatField()#db.Column(db.Float)  # 腹径
    femur = fields.FloatField()#db.Column(db.Float)   #股骨
    humerus = fields.FloatField()#db.Column(db.Float)   # 肱骨
    fi = fields.FloatField()#db.Column(db.Float)
    av = fields.FloatField()#db.Column(db.Float)
    a_b = fields.FloatField()#db.Column(db.Float)  # A/B
    placenta_position = fields.StringField()#db.Column(db.String(20))   # 胎盘位置
    placenta_thickness = fields.FloatField()#db.Column(db.Float)   # 胎盘厚度
    nf = fields.FloatField()#db.Column(db.Float)
    nasal_bone = fields.FloatField()#db.Column(db.Float)    #鼻骨
    b_check_description = fields.StringField()#db.Column(db.String(300))   # B超描述
    remarks = fields.StringField()#db.Column(db.String(500))   # 备注
    lmp = fields.DateField()#db.Column(db.Date)   #
    early_pregnancy = fields.StringField()#db.Column(db.String(50))   # 孕早期
    exception_description = fields.StringField()#db.Column(db.String(200))   # 异常描述
    infection_check = fields.StringField()#db.Column(db.String(200))   # 传染病等检查
    menses_ifrule = fields.BooleanField()#db.Column(db.Boolean)  # 平素月经_是否规则
    menses_days = fields.StringField()#db.Column(db.String(20))  # 月经天数
    menses_cycle = fields.StringField()#db.Column(db.String(20))  # 月经周期
    g = fields.IntegerField()#db.Column(db.Integer)
    p = fields.IntegerField()#db.Column(db.Integer)
    maternity_history = fields.StringField()#db.Column(db.String(300))  # 孕产史
    past_family_history = fields.StringField()#db.Column(db.String(100))  # 过去史家庭史
    diagnosis2 = fields.StringField()#db.Column(db.String(100))
    diagnosis1_g = fields.StringField()#db.Column(db.String(100))
    diagnosis1_p = fields.StringField()#db.Column(db.String(100))
    diagnosis1_pregnancy_week = fields.StringField()#db.Column(db.String(100))
    diagnosis1_pregnancy_day = fields.StringField()#db.Column(db.String(100))  # 诊断1_孕天
    operation_pregnancy_week = fields.IntegerField()#db.Column(db.Integer)  # 手术孕周
    operation_pregnancy_day = fields.IntegerField()#db.Column(db.Integer)  # 手术孕天
    diagnostic_doctor = fields.StringField()#db.Column(db.String(20))  # 诊断医生
    diagnostic_date = fields.DateField()#db.Column(db.Date)  # 诊断日期
    plan_operation_date = fields.DateField()#db.Column(db.Date)  # 拟手术日期
    operation_date = fields.DateField()#db.Column(db.Date)  # 手术日期
    temperature = fields.FloatField()#db.Column(db.Float)  # 体温
    blood_pressure_systolic = fields.IntegerField()#db.Column(db.Integer)  #血压_收缩压
    blood_pressure_diastolic = fields.IntegerField()#db.Column(db.Integer)  #血压_舒张压
    pulse = fields.IntegerField()#db.Column(db.Integer)  # 脉搏
    ray_injection_induction = fields.StringField()#db.Column(db.String(8))  # 雷注引产术
    intrauterine_treatment = fields.StringField()#db.Column(db.String(20))  # 宫内治疗
    times = fields.IntegerField()#db.Column(db.Integer)  # 次数
    surgical_placenta_location = fields.StringField()#db.Column(db.String(20))  #手术胎盘位置
    through_the_placenta = fields.StringField()#db.Column(db.String(8))  #经否胎盘
    placental_hemorrhage = fields.StringField()#db.Column(db.String(20))  #胎盘出血
    operation_time = fields.IntegerField()#db.Column(db.Integer)  # 手术时间
    extraction_sheep_water = fields.FloatField()#db.Column(db.Float)   #抽羊水量
    amniotic_fluid_properties = fields.StringField()#db.Column(db.String(20)) # 羊水性质
    preoperative_heart_rate = fields.StringField()#db.Column(db.String(50)) # 术前胎心率
    postoperative_heart_rate = fields.StringField()#db.Column(db.String(50)) # 术后胎心率
    operator = fields.StringField()#db.Column(db.String(20)) # 操作者
    special_records = fields.StringField()#db.Column(db.String(200))  # 特殊记录
    chromosome_reporting_date = fields.DateField()#db.Column(db.Date)  # 染色体报告日期
    chromosome_project = fields.StringField()#db.Column(db.String(50))  # 染色体项目
    chromosome = fields.StringField()#db.Column(db.String(300))  # 染色体
    afp_project = fields.StringField()#db.Column(db.String(50))
    afp = fields.StringField()#db.Column(db.String(50))
    poverty_gene_reporting_date = fields.DateField()#db.Column(db.Date)  # 地贫基因报告日期
    poverty_gene_project = fields.StringField()#db.Column(db.String(50))  # 地贫基因项目
    poverty_gene = fields.StringField()#db.Column(db.String(50))  # 地贫基因
    dna_project = fields.StringField()#db.Column(db.String(50))  # DNA项目
    cmv_tox_dna = fields.StringField()#db.Column(db.String(50))  # CMV、TOX-DNA
    other_check_project = fields.StringField()#db.Column(db.String(50))  # 其他检查项目
    other_check = fields.StringField()#db.Column(db.String(200))  # 其他检查
    department = fields.StringField()#db.Column(db.String(30))
    bed_no = fields.StringField()#db.Column(db.String(6))  #床号
    hospital_no = fields.StringField()#db.Column(db.String(6))  # 住院号
    exception_notification_date = fields.DateField()#db.Column(db.Date)  # 异常通知日期
    exception_notification = fields.StringField()#db.Column(db.String(200))
    follow_up_date = fields.DateTimeField()#db.Column(db.DateTime)  # 随访日期
    delivery_time = fields.TimeField()#db.Column(db.Time)  # 分娩时间
    sex = fields.StringField()#db.Column(db.String(8))
    weight = fields.FloatField()#db.Column(db.Float)  # 体重
    length = fields.FloatField()#db.Column(db.Float)  # 身长
    delivery_hospital = fields.StringField()#db.Column(db.String(50))  # 分娩医院
    delivery_pregnancy_week = fields.IntegerField()#db.Column(db.Integer)  # 分娩孕周
    delivery_mode = fields.StringField()#db.Column(db.String(50))  # 分娩方式
    neonatal_condition = fields.StringField()#db.Column(db.String(50))  # 新生儿情况
    loss_follow_up = fields.StringField()#db.Column(db.String(50))  # 失访
    other_description = fields.StringField()#db.Column(db.String(200))  # 其他描述
    entry_person = fields.StringField()# db.Column(db.String(20))  # 录入人
    modifier = fields.StringField()#db.Column(db.String(20))  # 修改人
    printing_times = fields.IntegerField()#db.Column(db.Integer) #打印次数
    sending_person = fields.StringField()#db.Column(db.String(10))  # 送检人
    receiver = fields.StringField()#db.Column(db.String(10))  # 接收人
    receiver_time = fields.StringField()#db.Column(db.String(10))  # 接收时间
    result_printing_times = fields.IntegerField()#db.Column(db.Integer)  #结果打印次数
    e3_nmol_1 = fields.FloatField()#db.Column(db.Float)  # E3_nmol/l
    e3_mo = fields.FloatField()#db.Column(db.Float)  #E3_Mo
    early_pregnancy_b_hcg_ng_l = fields.FloatField()#db.Column(db.Float)  # 早孕β-HCG_ng/l
    early_pregnancy_b_hcg_mo = fields.FloatField()#db.Column(db.Float)  # 早孕β-HCG_Mo
    ctr = fields.FloatField()#db.Column(db.Float)  # 心胸比
    exception_notification_person = fields.StringField()#db.Column(db.String(20))  # 异常通知人
    treatment_times = fields.IntegerField()#db.Column(db.Integer)  # 治疗次数
    id_number = fields.StringField()#db.Column(db.String(50))  #身份证号
    id_no = fields.StringField()#db.Column(db.String(50))  #ID号

