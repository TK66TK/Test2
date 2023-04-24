from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    db='iot23',
    charset='utf8'
)


@app.route('/')
def show():
    cur = conn.cursor()

    sql = "select * from student"
    cur.execute(sql)
    content = cur.fetchall()

    return render_template('show.html', content=content)


@app.route('/showinsert')
def showinsert():
    return render_template('insert.html')


@app.route('/subinsert', methods=['POST'])
def insert():
    name = request.form['name']
    id = request.form['id']
    birth = request.form['birth']

    cur = conn.cursor()
    sql = "INSERT INTO student (id,name,birth) VALUES (%s, %s, %s)"
    val = (id, name, birth)
    try:
        cur.execute(sql, val)
        conn.commit()
        return render_template('alert.html')
    except:
        conn.rollback()
        return render_template('error.html')


@app.route('/showdelete')
def showdelete():
    id = request.args.get("id")
    cur = conn.cursor()

    sql = "select * from student where id=" + str(id)
    cur.execute(sql)
    content = cur.fetchall()

    sql = "SHOW FIELDS FROM student"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]

    return render_template('delete.html', labels=labels, content=content)


@app.route('/subdelete')
def delete():
    id = request.args.get("id")

    cur = conn.cursor()
    sql = "DELETE FROM student WHERE id=" + str(id)
    try:
        cur.execute(sql)
        conn.commit()
        return render_template('alert.html')
    except:
        conn.rollback()
        return render_template('error.html')


@app.route('/showupdate')
def showupdate():
    id = request.args.get("id")
    cur = conn.cursor()

    sql = "select * from student where id=" + str(id)
    cur.execute(sql)
    content = cur.fetchall()

    return render_template('update.html', content=content)


@app.route('/subupdate', methods=['POST'])
def update():
    id = request.form['id']
    name = request.form['name']
    id2 = request.form['id2']
    birth = request.form['birth']
    cur = conn.cursor()

    sql = "update student set id='%s',name='%s' ,birth='%s' where id='%s'" % (id2, name, birth, id)
    try:
        cur.execute(sql)
        conn.commit()
        return render_template('alert.html')
    except:
        conn.rollback()
        return render_template('error.html')


@app.route('/showsearch')
def subsearch():
    id = request.args.get("id")
    cur = conn.cursor()
    sql = "SHOW FIELDS FROM student"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]
    sql1 = "select * from student where id=" + str(id)
    try:
      cur.execute(sql1)
      content = cur.fetchall()
      if len(content) == 0:
         return ("here")
      else:
         return render_template('search.html', labels=labels, content=content)
    except:
      conn.rollback()
      return render_template('error.html')

if __name__ == '__main__':
    app.run()

