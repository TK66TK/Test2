import pymysql
conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='iot23')
cursor=conn.cursor()
sql1 = 'SELECT * FROM student'
sql2 = "UPDATE student SET name='00olp' WHERE id=672"
sql3 = "INSERT INTO student (id, name) VALUES (%s, %s)"
val = (12,"John")
sql4 = "DELETE FROM student WHERE id=12"
#cursor.execute(sql3, val)
#cursor.execute(sql2)
cursor.execute(sql4)
conn.commit()
cursor.execute(sql1)
result = cursor.fetchall()
for row in result:
    print(row)
cursor.close()
conn.close()
