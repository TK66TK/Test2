from flask import Flask, request
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    db='iot23',
    charset='utf8'
)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    id = request.form['id']

    # 将数据插入到MySQL数据库中
    mycursor = conn.cursor()
    sql = "INSERT INTO students (id,name) VALUES (%s, %s)"
    val = (id,name)
    mycursor.execute(sql, val)
    conn.commit()

    return 'Data inserted successfully!'

