import mysql.connector
from flask import Flask, Response
import json

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='kissa',
    autocommit=True
    )

@app.route('/kenttä/<icao>')
def hakija(icao):
    parametri = (icao, )
    sql = f"SELECT ident as 'ICAO', name, municipality FROM airport WHERE ident = %s;"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, parametri)
    tulos = kursori.fetchone()
    return tulos

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3003)




