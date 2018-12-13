from app import db
from datetime import datetime, date, time
from flask import json


# Create user model.
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.now())

    # Flask-Login integration
    # NOTE: is_authenticated, is_active, and is_anonymous
    # are methods in Flask-Login < 0.3.0
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username


class Basefile(db.Model):
    __tablename__ = 'basefile'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(10), nullable=False)
    plan_code = db.Column(db.String(4), nullable=False)
    field_name = db.Column(db.String(50), nullable=False)
    basefile_name = db.Column(db.String(50))
    colid = db.Column(db.Integer)
    print_value = db.Column(db.String(50))
    default_value = db.Column(db.String(50))
    list_order = db.Column(db.Integer)
    sort_type = db.Column(db.String(10))
    sort_order = db.Column(db.Integer)
    show_width = db.Column(db.Integer, default=10)
    ifvisibled = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Basefile %r>' % self.basefile_name


class  Finehairrecord(db.Model):
    __tablename__ = 'finehairrecord'
    id = db.Column(db.Integer, primary_key=True)


class Umbilicalbloodrecord(db.Model):
    __tablename__ = 'umbilicalbloodrecord'
    id = db.Column(db.Integer, primary_key=True)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.__str__()
        if isinstance(obj, date):
            return obj.__str__()
        if isinstance(obj, time):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)


class Amnioticrecord(db.Model):
    __tablename__ = 'amnioticrecord'

    id = db.Column(db.Integer, primary_key=True)
    records = db.Column(db.String(30), nullable=False)
    record_no = db.Column(db.String(20), nullable=False)
    sort_no = db.Column(db.String(10))
    wife_name = db.Column(db.String(30))
    wife_age = db.Column(db.String(10))
    wife_birthday_year = db.Column(db.String(10))
    wife_birthday_month = db.Column(db.String(10))
    wife_origin = db.Column(db.String(30))
    wife_nation = db.Column(db.String(20))
    wife_profession = db.Column(db.String(30))
    wife_phone = db.Column(db.String(30))
    husband_name = db.Column(db.String(30))
    husband_age = db.Column(db.String(10))
    husband_birthday_year = db.Column(db.String(10))
    husband_birthday_month = db.Column(db.String(10))
    husband_origin = db.Column(db.String(30))
    husband_nation = db.Column(db.String(20))
    husband_profession = db.Column(db.String(30))
    husband_phone = db.Column(db.String(30))
    communication_address = db.Column(db.String(60))
    residential_telephone = db.Column(db.String(30))  # 住宅电话
    ifpoverty = db.Column(db.Boolean)   #双方地贫
    referral_status = db.Column(db.Boolean)   #是否转诊
    referral_hospital = db.Column(db.String(60))
    screen_date = db.Column(db.String(20))   # 筛查日期
    pregnancy_week = db.Column(db.String(10))  # 孕周
    pregnancy_day = db.Column(db.String(10))
    afp_od = db.Column(db.String(10))
    afp_mo = db.Column(db.String(10))
    b_hcg_od = db.Column(db.String(10))
    b_hcg_mo = db.Column(db.String(10))
    tribody_risk_21 = db.Column(db.String(10))
    tribody_risk_18 = db.Column(db.String(10))
    tribody_risk_13 = db.Column(db.String(10))
    ontd_risk = db.Column(db.String(8))
    pappa_miu_ml = db.Column(db.String(10))
    pappa_mo = db.Column(db.String(10))
    check_date = db.Column(db.String(20))
    check_hospital = db.Column(db.String(60))
    gene_detection_poverty = db.Column(db.String(50))    # 地贫基因检测
    red_crispy = db.Column(db.String(8))   #红脆
    wbc = db.Column(db.String(10))
    mcv = db.Column(db.String(10))
    mch = db.Column(db.String(10))
    hb = db.Column(db.String(10))
    bg = db.Column(db.String(10))
    rh = db.Column(db.String(20))
    hb_elect_a2 = db.Column(db.String(10))
    hb_elect_other = db.Column(db.String(20))
    husband_check_date = db.Column(db.String(20))
    husband_check_hospital = db.Column(db.String(60))
    husband_gene_detection_poverty = db.Column(db.String(50))    # 地贫基因检测
    husband_red_crispy = db.Column(db.String(8))   #红脆
    husband_wbc = db.Column(db.String(10))
    husband_mcv = db.Column(db.String(10))
    husband_mch = db.Column(db.String(10))
    husband_hb = db.Column(db.String(10))
    husband_bg = db.Column(db.String(10))
    husband_rh = db.Column(db.String(20))
    husband_hb_elect_a2 = db.Column(db.String(10))
    husband_hb_elect_other = db.Column(db.String(20))
    b_check_date = db.Column(db.String(20))   # B超日期
    b_check_hospital = db.Column(db.String(60))
    menolipsis_week = db.Column(db.String(10))  # 停经_周
    menolipsis_day = db.Column(db.String(10))  # 停经_天
    b_pregnancy_week = db.Column(db.String(10))  # B超孕周_周
    b_pregnancy_day = db.Column(db.String(10))
    bpd = db.Column(db.String(10))
    head_circumference = db.Column(db.String(10))  # 头围
    ventral_circumference = db.Column(db.String(10))   # 腹围
    ventral_diameter = db.Column(db.String(10))  # 腹径
    femur = db.Column(db.String(10))   #股骨
    humerus = db.Column(db.String(10))   # 肱骨
    fi = db.Column(db.String(10))
    av = db.Column(db.String(10))
    a_b = db.Column(db.String(10))  # A/B
    placenta_position = db.Column(db.String(20))   # 胎盘位置
    placenta_thickness = db.Column(db.String(10))   # 胎盘厚度
    nf = db.Column(db.String(10))
    nasal_bone = db.Column(db.String(10))    #鼻骨
    b_check_description = db.Column(db.String(300))   # B超描述
    remarks = db.Column(db.String(500))   # 备注
    lmp = db.Column(db.String(20))   #
    early_pregnancy = db.Column(db.String(50))   # 孕早期
    exception_description = db.Column(db.String(200))   # 异常描述
    infection_check = db.Column(db.String(200))   # 传染病等检查
    menses_ifrule = db.Column(db.Boolean)  # 平素月经_是否规则
    menses_days = db.Column(db.String(20))  # 月经天数
    menses_cycle = db.Column(db.String(20))  # 月经周期
    g = db.Column(db.String(10))
    p = db.Column(db.String(10))
    maternity_history = db.Column(db.String(300))  # 孕产史
    past_family_history = db.Column(db.String(100))  # 过去史家庭史
    diagnosis2 = db.Column(db.String(100))
    diagnosis1_g = db.Column(db.String(100))
    diagnosis1_p = db.Column(db.String(100))
    diagnosis1_pregnancy_week = db.Column(db.String(100))
    diagnosis1_pregnancy_day = db.Column(db.String(100))  # 诊断1_孕天
    operation_pregnancy_week = db.Column(db.String(10))  # 手术孕周
    operation_pregnancy_day = db.Column(db.String(10))  # 手术孕天
    diagnostic_doctor = db.Column(db.String(20))  # 诊断医生
    diagnostic_date = db.Column(db.String(20))  # 诊断日期
    plan_operation_date = db.Column(db.String(20))  # 拟手术日期
    operation_date = db.Column(db.String(20))  # 手术日期
    temperature = db.Column(db.String(10))  # 体温
    blood_pressure_systolic = db.Column(db.String(10))  #血压_收缩压
    blood_pressure_diastolic = db.Column(db.String(10))  #血压_舒张压
    pulse = db.Column(db.String(10))  # 脉搏
    ray_injection_induction = db.Column(db.String(8))  # 雷注引产术
    intrauterine_treatment = db.Column(db.String(20))  # 宫内治疗
    times = db.Column(db.String(10))  # 次数
    surgical_placenta_location = db.Column(db.String(20))  #手术胎盘位置
    through_the_placenta = db.Column(db.String(8))  #经否胎盘
    placental_hemorrhage = db.Column(db.String(20))  #胎盘出血
    operation_time = db.Column(db.String(10))  # 手术时间
    extraction_sheep_water = db.Column(db.String(10))   #抽羊水量
    amniotic_fluid_properties = db.Column(db.String(20)) # 羊水性质
    preoperative_heart_rate = db.Column(db.String(50)) # 术前胎心率
    postoperative_heart_rate = db.Column(db.String(50)) # 术后胎心率
    operator = db.Column(db.String(20)) # 操作者
    special_records = db.Column(db.String(200))  # 特殊记录
    chromosome_reporting_date = db.Column(db.String(20))  # 染色体报告日期
    chromosome_project = db.Column(db.String(50))  # 染色体项目
    chromosome = db.Column(db.String(300))  # 染色体
    afp_project = db.Column(db.String(50))
    afp = db.Column(db.String(50))
    poverty_gene_reporting_date = db.Column(db.String(20))  # 地贫基因报告日期
    poverty_gene_project = db.Column(db.String(50))  # 地贫基因项目
    poverty_gene = db.Column(db.String(50))  # 地贫基因
    dna_project = db.Column(db.String(50))  # DNA项目
    cmv_tox_dna = db.Column(db.String(50))  # CMV、TOX-DNA
    other_check_project = db.Column(db.String(50))  # 其他检查项目
    other_check = db.Column(db.String(200))  # 其他检查
    department = db.Column(db.String(30))
    bed_no = db.Column(db.String(6))  #床号
    hospital_no = db.Column(db.String(6))  # 住院号
    exception_notification_date = db.Column(db.String(20))  # 异常通知日期
    exception_notification = db.Column(db.String(200))
    follow_up_date = db.Column(db.String(20))  # 随访日期
    delivery_time = db.Column(db.String(20))  # 分娩时间
    sex = db.Column(db.String(8))
    weight = db.Column(db.String(10))  # 体重
    length = db.Column(db.String(10))  # 身长
    delivery_hospital = db.Column(db.String(50))  # 分娩医院
    delivery_pregnancy_week = db.Column(db.String(10))  # 分娩孕周
    delivery_mode = db.Column(db.String(50))  # 分娩方式
    neonatal_condition = db.Column(db.String(50))  # 新生儿情况
    loss_follow_up = db.Column(db.String(50))  # 失访
    other_description = db.Column(db.String(200))  # 其他描述
    entry_person = db.Column(db.String(20))  # 录入人
    modifier = db.Column(db.String(20))  # 修改人
    printing_times = db.Column(db.String(10)) #打印次数
    sending_person = db.Column(db.String(10))  # 送检人
    receiver = db.Column(db.String(10))  # 接收人
    receiver_time = db.Column(db.String(10))  # 接收时间
    result_printing_times = db.Column(db.String(10))  #结果打印次数
    e3_nmol_1 = db.Column(db.String(10))  # E3_nmol/l
    e3_mo = db.Column(db.String(10))  #E3_Mo
    early_pregnancy_b_hcg_ng_l = db.Column(db.String(10))  # 早孕β-HCG_ng/l
    early_pregnancy_b_hcg_mo = db.Column(db.String(10))  # 早孕β-HCG_Mo
    ctr = db.Column(db.String(10))  # 心胸比
    exception_notification_person = db.Column(db.String(20))  # 异常通知人
    treatment_times = db.Column(db.String(10))  # 治疗次数
    id_number = db.Column(db.String(50))  #身份证号
    id_no = db.Column(db.String(50))  #ID号

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return json.dumps(dict, cls=DateEncoder)

