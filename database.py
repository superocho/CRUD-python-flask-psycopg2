import psycopg2
connection = psycopg2.connect(
    host = 'localhost',
    database = 'tienda_demo',
    user = 'postgres',
    password = '0434',
    port = 5432
)

# COMPROBACION SUBTOTAL = CANTIDAD * PRECIO
# cursor = connection.cursor()
# 
# cursor.execute("""
#     SELECT D.subtotal
#     FROM Detalle_factura D
# """)
# 
# subtotales = cursor.fetchall()
# 
# cursor.execute("""
#     SELECT P.precio * D.cantidad
#     FROM Productos P JOIN Detalle_factura D ON P.id_producto = D.id_producto;
# """)
# 
# multiplicacion = cursor.fetchall()
# 
# if(len(multiplicacion) != len(subtotales)):
#     print("Lenghts are not equal")
# 
# contador = 0
# for i in range(len(multiplicacion)):
#     if(multiplicacion[i] != subtotales[i]):
#         print("NO SON IGUALES")
#         contador += 1
# 
# if(contador == 0):
#     print("Todos los valores son iguales")
#     
# cursor.close()
# connection.close()