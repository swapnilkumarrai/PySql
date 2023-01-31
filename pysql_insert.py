import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Cronaldo@07',database='entropik')
if conn.is_connected():
    print('connected')
    print(conn)
class mysql:
    def __init__(self):
        query=('create table if not exists swapnil(name char(20), age int, work varchar(15), address varchar(30))')
        print(query)
        cur=conn.cursor()
        cur.execute(query)
        print('executed successfully')
    def insert(self,name,age,work,address):
        query="insert into swapnil(name,age,work,address) values({},{},{},{})".format(name,age,work,address)
        cur=conn.cursor()
        cur.execute(query)
        conn.commit()
        print(query)
        print('values inserted')

a=mysql()
a.insert('swapnil',22,'backend','bangalore')
a.insert('pranjal',25,'seo','aurangabad')
a.insert('vaishnavi',22,'techassociate','gorakhpur')
a.insert('shalini',22,'frontend','bangalore')
    