from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Ruta principal que sirve el HTML
@app.route('/')
def index():
    return render_template('index.html')

# API que devuelve los lugares
@app.route('/api/lugares')
def api_lugares():
    # Conexión a la base de datos
    conn = sqlite3.connect('negocios.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nombre, lat, lon, cp, municipio, actividad FROM negocios")
    lugares = [
        {
            "id": row[0],
            "nombre": row[1],
            "lat": row[2],
            "lon": row[3],
            "cp": row[4],
            "municipio": row[5],
            "actividad": row[6]
        }
        for row in cursor.fetchall()
    ]
    
    conn.close()
    return jsonify(lugares)

if __name__ == '__main__':
    app.run(debug=True)
