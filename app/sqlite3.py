import sqlite3
import pymysql


basedir = os.path.abspath(os.path.dirname(__file__))  #项目的根目录
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


# 连接数据库
con = sqlite3.connect(SQLALCHEMY_DATABASE_URI)
cur = con.cursor()

# 查询记录
select_sql = "select * from users"
cur.execute(select_sql)

# 返回一个list，list中的对象类型为tuple（元组）
date_set = cur.fetchall()
for row in date_set:
    print(row)

#获得查询结果表的列名：
cur.execute("select * from users")
col_name_list = [tuple[0] for tuple in cur.description]
print(col_name_list)
#获得所有列名：
cur.execute("PRAGMA table_info(table)")
print(cur.fetchall())





cur.close()
con.close()
