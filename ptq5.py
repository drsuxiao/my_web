import csv
from app import db
from app.data_models import Basefile


my_data = []
with open('amoc.txt', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    my_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        my_data.append(row)

    print(my_data)

db.session.query(Basefile).delete()
for row in my_data:
    type_name = row[1]
    plan_code = row[2]
    field_name = row[3]
    basefile_name = row[4]
    colid = row[5]
    print_value = row[6]
    default_value = row[7]
    list_order = row[8]
    sort_type = row[9]
    sort_order = row[10]
    show_width = row[11]
    if row[12] == 'True':
        ifvisibled = 1
    else:
        ifvisibled = 0
    if colid == '':
        colid = -1
    if list_order == '':
        list_order = -1
    if sort_order == '':
        sort_order = -1
    if show_width == '':
        show_width = -1
    basefile = Basefile(type_name=type_name, plan_code=plan_code, field_name=field_name, basefile_name=basefile_name,
                        colid=colid, print_value=print_value, default_value=default_value,
                        list_order=list_order, sort_type=sort_type, sort_order=sort_order, show_width=show_width, ifvisibled=ifvisibled)
    print(basefile)
    db.session.add(basefile)
db.session.commit()
print(db.session.query(Basefile).count())