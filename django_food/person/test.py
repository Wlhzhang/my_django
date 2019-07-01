# import os
# import django
# import MySQLdb
# from MySQLdb.cursors import DictCursor
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_food.settings')
# django.setup()
#
# # 将一个数据表里面的数据转移到另外一个数据表
# num = 1
# con = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='142857',db='django_food',charset='utf8')
# cur = con.cursor()
# data_sql='select * from travel_area'
# cur.execute(data_sql)
# data_list=cur.fetchall()
# try:
#     sql = "insert into person_city values(%s,%s,%s,%s,%s);"
#     for data_obj in data_list:
#         cur.execute(sql,data_obj)
#     con.commit()
# finally:
#     cur.close()
#     con.close()