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

# pg: Devuelve todos los productos de la tabla Productos
def getProductos():
    cursor.execute("SELECT * FROM Productos")
    return cursor.fetchall()

# pg: Devuelve todas las tuplas haciendo JOIN entre productos y categorias
def getProductosJOINCategorias():
    cursor.execute(
        "SELECT * FROM Productos P JOIN Categorias C ON P.id_categoria = C.id_categoria"
    )
    return cursor.fetchall()

# pg: Agregar producto a la tabla productos
def addProducto(conn, producto, precio, stock, categoria):
    cursor.execute(
        "INSERT INTO Productos (nombre_producto, precio, stock, id_categoria) VALUES (%s, %s, %s, %s)",
        (producto, precio, stock, categoria),    
    )
    conn.commit()

# pg: Eliminar producto de la tabla productos pasando la id del prodcuto que se quiera eliminar
def deleteProducto(conn, id):
    cursor.execute("DELETE FROM Productos WHERE id_producto = %s", (id,))
    conn.commit()

# pg: Devuelve todas las categorias de la tabla Categorias
def getCategorias():
    cursor.execute("SELECT * FROM Categorias")
    return cursor.fetchall()

def getCategoriasJOIN():
    cursor.execute("""
        SELECT C.nombre_categoria, SUM(D.subtotal)
        FROM Categorias C JOIN Productos P ON C.id_categoria = P.id_categoria
        JOIN detalle_factura D ON P.id_producto = D.id_producto
        GROUP BY C.nombre_categoria
        ORDER BY SUM(D.subtotal) DESC
    """)
    return cursor.fetchall()

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# web: Muestra todos los clientes
@app.route('/clientes')
def mostrarClientes():
    for categoria in getCategoriasJOIN():
        print(categoria)
    clientes = getClientes()
    return render_template('clientes.html', clientes=clientes)

# web: Agrega un cliente a la tabla Clientes con los datos ingresados en la pagina
@app.route('/clientes/add', methods=['POST'])
def addClienteWeb():
    nombre = request.form['nombre']
    correo = request.form['correo']
    ciudad = request.form['ciudad']
    if(nombre and correo and ciudad):
        addCliente(conn, nombre, correo, ciudad)
    return redirect(url_for('mostrarClientes'))

# web: Eliminar cliente de la tabla Clientes
@app.route('/clientes/delete/<string:id>', methods=['POST'])
def deleteClienteWeb(id):
    deleteCliente(conn, id)
    return redirect(url_for('mostrarClientes'))

# web: Mostrar todos los productos
@app.route('/productos')
def mostrarProductos():
    productosJOIN = getProductosJOINCategorias()
    categorias = getCategorias()
    return render_template('productos.html', categorias=categorias, productos=productosJOIN)

# web: Agregar producto a la tabla Productos con los datos ingresados en la pagina
@app.route('/productos/add', methods=['POST'])
def addProductoWeb():
    producto = request.form['producto']
    precio = request.form['precio']
    stock = request.form['stock']
    categoria = request.form['categoria']
    if(producto and precio and stock and categoria):
        addProducto(conn, producto, precio, stock, categoria)
    return redirect(url_for('mostrarProductos'))

# web: Eliminar producto por id
@app.route('/productos/delete/<string:id>', methods=['POST'])
def deleteProductoWeb(id):
    deleteProducto(conn, id)
    return redirect(url_for('mostrarProductos'))

@app.route('/categorias')
def mostrarCategorias():
    categorias = getCategoriasJOIN()
    return render_template('categorias.html', categorias=categorias)

# @app.route('/categorias/add')
# def mostrarCategorias():
#     return redirect(url_for('mostrarCategorias'))

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

cursor.close()
conn.close()