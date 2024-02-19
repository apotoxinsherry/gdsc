from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('surveillance_data.db')

# Route to fetch data from the SQLite database
@app.route('/data', methods=['GET'])
def get_data():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM surveillance_data')  # Replace 'your_table' with the actual table name
    data = cursor.fetchall()
    conn.close()

    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin', '*')


    return res

if __name__ == '__main__':
    app.run(debug=True, port=1237)
