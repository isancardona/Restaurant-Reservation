from flask import Flask, render_template, request
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/registered")
def registered():
    return render_template('registered.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/guest")
def guest():
    return render_template('guest.html')

if __name__ == "__main__":
    app.run(debug=True)