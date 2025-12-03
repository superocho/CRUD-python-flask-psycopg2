from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import date
import database as db
import json

app = Flask(__name__)
conn = db.connection
cursor = conn.cursor()

# pg: Devuelve listado de todos los clientes
def getClientes():
    cursor.execute("""
        SELECT * FROM Clientes C
        ORDER BY C.id_cliente ASC
    """)
    return cursor.fetchall()

# pg: Insertar tupla en tabla clientes
def addCliente(conn, nombre, correo, ciudad, fecha_registro=None):
    if fecha_registro is None:
        fecha_registro = date.today()
    cursor.execute(
        "INSERT INTO Clientes(nombre, correo, ciudad, fecha_registro) VALUES (%s, %s, %s, %s)",
        (nombre, correo, ciudad, fecha_registro),
    )
    conn.commit()

# pg: Editar tupla de tabla clientes pasando los nuevos datos que queremos cambiar
def editCliente(conn, id_cliente, nombre, correo, ciudad):
    cursor.execute(
        "UPDATE Clientes SET nombre = %s, correo = %s, ciudad = %s WHERE id_cliente = %s", 
        (nombre, correo, ciudad, id_cliente)
    )
    conn.commit()

# pg: Devuelve todos los productos de la tabla Productos
def getProductos():
    cursor.execute("""
        SELECT * 
        FROM Productos P
        ORDER BY P.id_producto ASC
    """)
    return cursor.fetchall()

# pg: Devuelve todas las tuplas haciendo JOIN entre productos y categorias
def getProductosJOINCategorias():
    cursor.execute("""
        SELECT * 
        FROM Productos P 
        JOIN Categorias C ON P.id_categoria = C.id_categoria
        ORDER BY P.id_producto ASC
    """)
    return cursor.fetchall()

# pg: Agregar producto a la tabla productos
def addProducto(conn, producto, precio, stock, categoria):
    cursor.execute(
        "INSERT INTO Productos (nombre_producto, precio, stock, id_categoria) VALUES (%s, %s, %s, %s)",
        (producto, precio, stock, categoria),
    )
    conn.commit()

# pg: Editar tupla de tabla Productos pasando los nuevos datos que queremos cambiar
def editProducto(conn, id_producto, nombre, precio, stock, id_categoria):
    cursor.execute(
        "UPDATE Productos SET nombre_producto = %s, precio = %s, stock = %s, id_categoria = %s WHERE id_producto = %s", 
        (nombre, precio, stock, id_categoria, id_producto)
    )
    conn.commit()

# pg: Devuelve todas las categorias de la tabla Categorias
def getCategorias():
    cursor.execute("SELECT * FROM Categorias")
    return cursor.fetchall()

# pg: Devuelve el nombre y ventas totales de cada categoria de mayor a menor (si SUM(D.subtotal) es 0 no aparece)
def getCategoriasJOIN():
    cursor.execute("""
        SELECT C.nombre_categoria, SUM(D.subtotal)
        FROM Categorias C JOIN Productos P ON C.id_categoria = P.id_categoria
        JOIN detalle_factura D ON P.id_producto = D.id_producto
        GROUP BY C.nombre_categoria
        ORDER BY SUM(D.subtotal) DESC
    """)
    return cursor.fetchall()

# pg: Elimina un detalle_factura pasandole la id
def deleteDetalleFactura(conn, id):
    cursor.execute("DELETE FROM Detalle_factura WHERE id_detalle = %s", (id,))
    conn.commit()

# pg: Elimina una factura y todos los detalle_facturas enlazados con la id correspondiente
def deleteFactura(conn, id):
    cursor.execute("""SELECT *
    FROM Facturas F
    JOIN Detalle_factura D ON F.id_factura = D.id_factura
    WHERE F.id_factura = %s
    """, (id,))
    for detalle_factura in cursor.fetchall():
        deleteDetalleFactura(conn, detalle_factura[4])
    cursor.execute("DELETE FROM Facturas WHERE id_factura = %s", (id,))
    conn.commit()

# Elimina un cliente y todas las tuplas de facturas y detalle_factura correspondientes
def deleteCliente(conn, id):
    cursor.execute("""SELECT *
        FROM Clientes C
        JOIN Facturas F ON C.id_cliente = F.id_cliente
        WHERE C.id_cliente = %s
    """, (id,))
    for factura in cursor.fetchall():
        deleteFactura(conn, factura[5])
    cursor.execute("DELETE FROM Clientes WHERE id_cliente = %s", (id,))
    conn.commit()

# pg: Devuelve todas las regiones
def getRegiones():
    cursor.execute("SELECT * FROM region_cl ORDER BY id_re ASC")
    return cursor.fetchall()

# pg: Devuelve todas las provincias de una region correspondiente
def getProvinciasPorRegion(id_region):
    cursor.execute("""
        SELECT *
        FROM provincia_cl P
        WHERE P.id_re = %s
        ORDER BY P.str_descripcion ASC
    """, (id_region,))
    return cursor.fetchall()

# pg: Devuelve todas las comunas de una provincia correspondiente
def getComunasPorProvincia(id_provincia):
    cursor.execute("""
        SELECT *
        FROM comuna_cl C
        WHERE C.id_pr = %s
        ORDER BY C.str_descripcion ASC
    """, (id_provincia,))
    return cursor.fetchall()

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# web: Muestra todos los clientes
@app.route('/clientes')
def mostrarClientes():
    clientes = getClientes()
    return render_template('clientes.html', clientes=clientes)

# web: Agrega un cliente a la tabla Clientes con los datos ingresados en la pagina
@app.route('/clientes/add', methods=['POST'])
def addClienteWeb():
    nombre = request.form['nombre']
    correo = request.form['correo']
    region = request.form['region']
    provincia = request.form['provincia']
    comuna = request.form['comuna']
    if(nombre and correo and region and provincia and comuna):
        addCliente(conn, nombre, correo, comuna)
    else:
        return "Error: debe seleccionar todos los campos necesarios", 400
    return redirect(url_for('mostrarClientes'))

# web: Editar los atributos de un cliente de la tabla Clientes con los datos ingresados en la pagina
@app.route('/clientes/edit/<string:id>', methods=['POST'])
def editClienteWeb(id):
    nombre = request.form['nombre']
    correo = request.form['correo']
    ciudad = request.form['ciudad']
    if(nombre and correo and ciudad):
        editCliente(conn, id, nombre, correo, ciudad)
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

# web: Editar los atributos de un producto de la tabla Productos con los datos ingresados en la pagina
@app.route('/productos/edit/<string:id>', methods=['POST'])
def editProductoWeb(id):
    nombre = request.form['nombre']
    precio = request.form['precio']
    stock = request.form['stock']
    id_categoria = request.form['id_categoria']
    if(nombre and precio and stock and id_categoria):
        editProducto(conn, id, nombre, precio, stock, id_categoria)
    return redirect(url_for('mostrarProductos'))

# web: Eliminar producto por id
# @app.route('/productos/delete/<string:id>', methods=['POST'])
# def deleteProductoWeb(id):
#     deleteProducto(conn, id)
#    return redirect(url_for('mostrarProductos'))

@app.route('/categorias')
def mostrarCategorias():
    categorias = getCategoriasJOIN()
    labels = []
    ventas = []
    for c in categorias:
        labels.append(c[0])
        ventas.append(int(c[1]))
    # Convertir a JSON en orden inverso
    labels_json = json.dumps(labels[::-1])
    ventas_json = json.dumps(ventas[::-1])
    return render_template('categorias.html', categorias=categorias, labels=labels_json, ventas=ventas_json)

@app.route('/api/regiones')
def getRegionesAPI():
    regiones = getRegiones()
    return jsonify([{'id': r[0], 'nombre': r[1]} for r in regiones])

@app.route('/api/provincias/<int:id_region>')
def getProvinciasAPI(id_region):
    provincias = getProvinciasPorRegion(id_region)
    return jsonify([{'id': p[0], 'nombre': p[2]} for p in provincias])

@app.route('/api/comunas/<int:id_provincia>')
def getComunasAPI(id_provincia):
    comunas = getComunasPorProvincia(id_provincia)
    return jsonify([{'id': c[0], 'nombre': c[2]} for c in comunas])

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

cursor.close()
conn.close()