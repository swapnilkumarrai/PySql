import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Cronaldo@07',database='entropiktech')
if conn.is_connected():
    print('succesfull connection')
    print(conn)
class swap:
    def delete(self,emp_id):
        query="delete from user where emp_id={}".format(emp_id)
        cur=conn.cursor()
        cur.execute(query)
        conn.commit()

#     def __init__(self):
#         a=conn
#         query=('create table if not exists user(emp_name varchar(10), emp_id int, emp_dep varchar(15), emp_city varchar(15))')
#         cur=a.cursor()
#         cur.execute(query)
#         print('created')
#     def insert(self,emp_name,emp_id,emp_dep,emp_city):
#         query="insert into user(emp_name,emp_id,emp_dep,emp_city) values('{}',{},'{}','{}')".format(emp_name,emp_id,emp_dep,emp_city)
#         curr=conn.cursor()
#         curr.execute(query)
#         conn.commit()
#         print(query)
#         print('values inserted')
    def print(self):
        query='select * from user'
        cur=conn.cursor()
        cur.execute(query)
        for row in cur:
            print('emp_name: ',row[0])
            print('emp_id: ',row[1])
            print('emp_role: ',row[2])
            print('emp_city: ',row[3])
            print('\n')

b=swap()
# b.insert('gaurav',10001,'tester','pune')
# b.insert('jaggi',10002,'tester','bangalore')
# b.insert('satish',10003,'devops','bangalore')
# b.insert('parikshit',10004,'marketing','delhi')
# b.insert('divyanshu',10005,'webdeveloper','mohali')
# class fetch:
b.delete(10004)
b.print()

