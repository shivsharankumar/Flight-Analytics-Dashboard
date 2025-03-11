import pymysql

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Svini@1995',
        database='indigo'
    )
    mycursor = conn.cursor()
    print('connection established!!!')
except:
    print("Connection Error")


#serch retreive
mycursor.execute("select * from airport where aid>1")
data=mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

#update 
mycursor.execute("""update airport set """)