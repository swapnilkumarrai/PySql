import mysql.connector
conn=mysql.connector.connect(host='localhost',password='Cronaldo@07',username='root',database='entropiktech')
if conn.is_connected():
    print('connected succesfully')
class mysql:
    def __init__(self):
        query=('create table if not exists futbol(player_name varchar(30), player_club varchar(30), jersey_no int, strength varchar(40),weakness varchar(40))')
        cur=conn.cursor()
        cur.execute(query)
        print('created table successfully')
    def insert(self,player_name,player_club,jersey_no,strength,weakness):
        query="insert into futbol(player_name,player_club,jersey_no,strength,weakness) values('{}','{}',{},'{}','{}')".format(player_name,player_club,jersey_no,strength,weakness)
        cur=conn.cursor()
        cur.execute(query)
        conn.commit()
    def print(self):
        query='select * from futbol'
        cur=conn.cursor()
        cur.execute(query)
        for row in cur:
            print('Player_name:',row[0])
            print('player_club: ',row[1])
            print('player_number: ',row[2])
            print('strength: ',row[3])
            print('weakness: ',row[4])
            print('\n')
    def update(self,player_name,player_club,jersey_no,strength,weakness,jer_no):
        query="update futbol set player_name='{}',player_club='{}',jersey_no={},strength='{}',weakness='{}' where jersey_no={}".format(player_name,player_club,jer_no,strength,weakness,jersey_no)
        cur=conn.cursor()
        cur.execute(query)
        conn.commit()
        print('updated successfully')
a=mysql()
# for i in range(0,10):
#     b=input('player name: ')
#     c=input('player club: ')
#     d=int(input('player number: '))
#     e=input('strength: ')
#     f=input('weakness: ')
#     a.insert(b,c,d,e,f)
b=input('enter new name')
c=input('enter new club')
d=input('enter new strength')
e=input('enter new weakness')
f=int(input('enter new number'))
a.update(b,c,4,d,e,f)
a.print()
