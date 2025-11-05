from flask import Flask, jsonify, render_template, url_for
import psycopg2
from datetime import date
import database as db

app = Flask(__name__)
cursor = db.conn.cursor()

# pg: Insertar en tabla clientes
def addCliente(conn, nombre, correo, ciudad, fecha_registro=None):
    if fecha_registro is None:
        fecha_registro = date.today()
    cursor.execute(
        "INSERT INTO Clientes(nombre, correo, ciudad, fecha_registro) VALUES (%s, %s, %s, %s)",
        (nombre, correo, ciudad, fecha_registro),
    )
    db.conn.commit()
    cursor.close()

# pg: Devuelve listado de todos los clientes
def getClientes(conn):
    cursor.execute("SELECT * FROM Clientes")
    return cursor.fetchall()

# web: Muestra todos los clientes
@app.route('/clientes')
def mostrarClientes():
    clientes = getClientes(db.conn)
    return render_template('clientes.html', clientes=clientes)




if __name__ == '__main__':
    app.run(debug=True)
    
db.conn.close()