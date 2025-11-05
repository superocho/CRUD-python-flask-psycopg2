from flask import Flask, render_template, request, redirect, url_for
from datetime import date
import database as db

app = Flask(__name__)
conn = db.connection
cursor = conn.cursor()

# pg: Insertar tupla en tabla clientes
def addCliente(conn, nombre, correo, ciudad, fecha_registro=None):
    if fecha_registro is None:
        fecha_registro = date.today()
    cursor.execute(
        "INSERT INTO Clientes(nombre, correo, ciudad, fecha_registro) VALUES (%s, %s, %s, %s)",
        (nombre, correo, ciudad, fecha_registro),
    )
    conn.commit()

# pg: Eliminar tupla en tabla clientes pasando la id del cliente que queremos eliminar
def deleteCliente(conn, id_cliente):
    cursor.execute("DELETE FROM Clientes WHERE id_cliente = %s;", (id_cliente,))
    conn.commit()

# pg: Devuelve listado de todos los clientes
def getClientes():
    cursor.execute("SELECT * FROM Clientes")
    return cursor.fetchall()

# --------------------------------------------------------------------------------------------------------

# web: Muestra todos los clientes
@app.route('/clientes')
def mostrarClientes():
    clientes = getClientes()
    return render_template('clientes.html', clientes=clientes)

# web: Agrega un cliente a la tabla Clientes con los datos ingresados en la pagina
@app.route('/add', methods=['POST'])
def addClienteWeb():
    nombre = request.form['nombre']
    correo = request.form['correo']
    ciudad = request.form['ciudad']
    if(nombre and correo and ciudad):
        addCliente(conn, nombre, correo, ciudad)
    return redirect(url_for('mostrarClientes'))

# web: Eliminar cliente de la tabla Clientes
@app.route('/delete/<string:id>', methods=['POST'])
def deleteClienteWeb(id):
    print(id)
    deleteCliente(conn, id)
    print("SALIO")
    return redirect(url_for('mostrarClientes'))

if __name__ == '__main__':
    app.run(debug=True)

cursor.close()
conn.close()