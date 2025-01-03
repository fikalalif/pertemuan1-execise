from flask import Flask, render_template, request, redirect,url_for,jsonify,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'web_uas'

mysql = MySQL(app)

@app.route('/cek database')
def cek_database():
    cur = mysql.connection.cursor()
    cur.execute('SELECT 1')
    return jsonify('message : database connected')

@app.route('/get-product')
def getProduct():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM product')
    product = cur.fetchall()
    return jsonify (product)

@app.route('/home-page')
def homepage():
    cur = mysql.connection.cursor()
    # query = '''SELECT * FROM product'''
    #STRING TIGA BISA MENAMBAHKAN BEBERAPA KODE DITIAP BARIS NYA
    cur.execute('SELECT * FROM product')
    product = cur.fetchall()

    return render_template('homepage.html', product = product)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/footer')
# def footer():
#     return render_template('templates\base\footer.html')

if __name__ == "__main__":
    app.run(debug=True)