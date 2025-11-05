import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="tienda_demo",
    user="postgres",
    password="0434",
)