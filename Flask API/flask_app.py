from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return "Possible paths: <br>" + \
           "/dji_data_close<br>" + \
           "/sp_crypto_data<br>" + \
           "/bitcoin<br>" + \
           "/ethereum<br>" + \
           "/dji_vol<br>" + \
           "/crypto_vol<br>" + \
           "/bitcoin_vol<br>" + \
           "/ethereum_vol"

@app.route('/dji_data_close', methods=['GET'])
def get_dji_data_close():
    conn = sqlite3.connect('/home/levimcleod/mysite/market.db')
    c = conn.cursor()
    c.execute('SELECT * FROM dji_data_close')
    rows = c.fetchall()
    data = [{'date': row[0], 'close': row[1]} for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/sp_crypto_data', methods=['GET'])
def get_sp_crypto_data():
    conn = sqlite3.connect('/home/levimcleod/mysite/market.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sp_crypto_data')
    rows = c.fetchall()
    data = [{'date': row[0], 'value': row[1]} for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/bitcoin', methods=['GET'])
def get_bitcoin():
    conn = sqlite3.connect('/home/levimcleod/mysite/market.db')
    c = conn.cursor()
    c.execute('SELECT * FROM bitcoin')
    rows = c.fetchall()
    data = [{'date': row[0], 'price': row[1]} for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/ethereum', methods=['GET'])
def get_ethereum():
    conn = sqlite3.connect('/home/levimcleod/mysite/market.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ethereum')
    rows = c.fetchall()
    data = [{'date': row[0], 'price': row[1]} for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/dji_vol', methods=['GET'])
def get_dji_vol():
    conn = sqlite3.connect('/home/levimcleod/mysite/market.db')
    c = conn.cursor()
    c.execute('SELECT * FROM dji_vol')
    rows = c.fetchall()
    data = [{'date': row[0], 'close': row[1]} for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/crypto_vol', methods=['GET'])
def get_crypto_vol():
    conn = sqlite3.connect('/home/levimcleod/mysite/market.db')
    c = conn.cursor()
    c.execute('SELECT * FROM crypto_vol')
    rows = c.fetchall()
    data = [{'date': row[0], 'value': row[1]} for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/bitcoin_vol', methods=['GET'])
def get_bitcoin_vol():
    conn = sqlite3.connect('/home/levimcleod/mysite/market.db')
    c = conn.cursor()
    c.execute('SELECT * FROM bitcoin_vol')
    rows = c.fetchall()
    data = [{'date': row[0], 'price': row[1]} for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/ethereum_vol', methods=['GET'])
def get_ethereum_vol():
    conn = sqlite3.connect('/home/levimcleod/mysite/market.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ethereum_vol')
    rows = c.fetchall()
    data = [{'date': row[0], 'price': row[1]} for row in rows]
    conn.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run()