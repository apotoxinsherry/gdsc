from flask import Flask, render_template, request, redirect, session
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect('/login')


@app.route("/reports")
def reports():
    if 'username' in session:
        return render_template('reports.html', username=session['username'])
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = authenticate_user(username, password)
        if user:
            session['username'] = user[0]
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

def authenticate_user(username, password):
    try:
        conn = sqlite3.connect('login_system.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
    except sqlite3.Error as e:
        print("Error authenticating user:", e)
        return None

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
