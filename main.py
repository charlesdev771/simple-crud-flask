from flask import Flask, url_for, redirect, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder="templates")
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
mysql = MySQL(app)



@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM computer")
    data = cur.fetchall()
    cur.close()
    return render_template('home.html', computers=data)



@app.route('/simpan', methods=["POST"])
def simpan():
    nama = request.form['nama']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO computer (data) VALUES (%s)", (nama,))
    mysql.connection.commit()
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)
