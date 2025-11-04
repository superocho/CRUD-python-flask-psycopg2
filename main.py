from flask import Flask, jsonify, render_template, url_for
import psycopg2
from datetime import date

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="tienda_demo",
    user="postgres",
    password="0434",
)
# pg: Insertar en tabla clientes
def addCliente(conn, nombre, correo, ciudad, fecha_registro=None):
    cursor = conn.cursor()
    if fecha_registro is None:
        fecha_registro = date.today()
    cursor.execute(
        "INSERT INTO Clientes(nombre, correo, ciudad, fecha_registro) VALUES (%s, %s, %s, %s)",
        (nombre, correo, ciudad, fecha_registro),
    )
    conn.commit()
    cursor.close()

# pg: Devuelve listado de todos los clientes
def getClientes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes")
    return cursor.fetchall()

# web: Muestra todos los clientes
@app.route('/clientes')
def mostrarClientes():
    clientes = getClientes(conn)
    return render_template('clientes.html', clientes=clientes)




if __name__ == '__main__':
    app.run(debug=True)
    
conn.close()