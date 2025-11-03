from flask import Flask, jsonify, render_template, url_for
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="tienda_demo",
    user="postgres",
    password="0434",
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM Clientes")



@app.route('/clientes')
def mostrarClientes():
    clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
    
cursor.close()
conn.close()