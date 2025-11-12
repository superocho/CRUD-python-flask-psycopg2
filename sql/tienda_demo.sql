CREATE TABLE clientes (
    id_cliente INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE,
    ciudad VARCHAR(50),
    fecha_registro DATE
);
CREATE TABLE categorias (
    id_categoria INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_categoria VARCHAR(50) NOT NULL
);
CREATE TABLE productos (
    id_producto INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);
CREATE TABLE facturas (
    id_factura INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_cliente INT,
    fecha DATE NOT NULL,
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
CREATE TABLE detalle_factura (
    id_detalle INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_factura INT,
    id_producto INT,
    cantidad INT NOT NULL,
    subtotal DECIMAL(10,2),
    FOREIGN KEY (id_factura) REFERENCES facturas(id_factura),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

INSERT INTO clientes (nombre, correo, ciudad, fecha_registro) VALUES
('Juan Perez', 'juanp@mail.com', 'Concepcion', '2024-01-15'),
('Maria Lopez', 'marial@mail.com', 'Santiago', '2024-03-20'),
('Carlos Diaz', 'carlosd@mail.com', 'Valparaiso', '2024-05-10'),
('Ana Torres', 'anat@mail.com', 'Concepcion', '2024-07-25'),
('Luis Fernandez', 'luisf@mail.com', 'Temuco', '2024-04-14'),
('Sofia Gutierrez', 'sofiag@mail.com', 'Santiago', '2024-02-10'),
('Pedro Soto', 'pedros@mail.com', 'Antofagasta', '2024-06-05'),
('Camila Reyes', 'camilar@mail.com', 'La Serena', '2024-08-18'),
('Diego Castro', 'diegoc@mail.com', 'Iquique', '2024-03-11'),
('Valentina Vega', 'valenv@mail.com', 'Santiago', '2024-01-29'),
('Ignacio Morales', 'ignaciom@mail.com', 'Concepcion', '2024-07-01'),
('Francisca Silva', 'frans@mail.com', 'Valdivia', '2024-06-12'),
('Ricardo Herrera', 'ricardoh@mail.com', 'Talca', '2024-05-25'),
('Daniela Pizarro', 'danip@mail.com', 'Arica', '2024-04-08'),
('Jorge Ruiz', 'jorger@mail.com', 'Santiago', '2024-03-19'),
('Claudia Navarro', 'claudian@mail.com', 'Concepcion', '2024-09-01'),
('Matias Rojas', 'matiasr@mail.com', 'Santiago', '2024-07-07'),
('Fernanda Molina', 'fernandam@mail.com', 'Chillan', '2024-08-21'),
('Pablo Cardenas', 'pabloc@mail.com', 'Puerto Montt', '2024-06-17'),
('Isidora Fuentes', 'isidoraf@mail.com', 'Rancagua', '2024-05-30');

INSERT INTO categorias (nombre_categoria) VALUES
('Electronica'),
('Ropa'),
('Alimentos'),
('Hogar'),
('Deportes'),
('Libros'),
('Juguetes'),
('Accesorios'),
('Automotriz'),
('Belleza'),
('Mascotas'),
('Computacion'),
('Instrumentos Musicales'),
('Ferreteria'),
('Jardineria'),
('Oficina'),
('Videojuegos'),
('Calzado'),
('Fotografia'),
('Salud');

INSERT INTO productos (nombre_producto, precio, stock, id_categoria) VALUES
('Laptop', 750000, 15, 1),
('Celular', 350000, 30, 1),
('Polera', 15000, 50, 2),
('Pantalon', 25000, 40, 2),
('Leche', 1200, 100, 3),
('Pan', 1000, 80, 3),
('Silla', 25000, 20, 4),
('Balon Futbol', 20000, 25, 5),
('Libro Programacion', 18000, 35, 6),
('Muñeca', 12000, 15, 7),
('Reloj Pulsera', 45000, 12, 8),
('Aceite Motor', 28000, 18, 9),
('Shampoo', 3000, 60, 10),
('Comida Perro', 20000, 40, 11),
('Mouse Gamer', 15000, 45, 12),
('Guitarra', 95000, 10, 13),
('Martillo', 8000, 25, 14),
('Maceta', 5000, 30, 15),
('Silla Oficina', 45000, 15, 16),
('Consola Juegos', 400000, 8, 17);

INSERT INTO facturas (id_cliente, fecha, total) VALUES
(1, '2024-08-01', 0),
(2, '2024-08-02', 0),
(3, '2024-08-05', 0),
(4, '2024-08-07', 0),
(5, '2024-08-08', 0),
(6, '2024-08-10', 0),
(7, '2024-08-11', 0),
(8, '2024-08-12', 0),
(9, '2024-08-13', 0),
(10, '2024-08-15', 0),
(11, '2024-08-16', 0),
(12, '2024-08-17', 0),
(13, '2024-08-18', 0),
(14, '2024-08-19', 0),
(15, '2024-08-20', 0),
(16, '2024-08-22', 0),
(17, '2024-08-23', 0),
(18, '2024-08-25', 0),
(19, '2024-08-26', 0),
(20, '2024-08-28', 0),
(1, '2024-09-01', 0),
(2, '2024-09-02', 0),
(3, '2024-09-03', 0),
(4, '2024-09-04', 0),
(5, '2024-09-05', 0),
(6, '2024-09-06', 0),
(7, '2024-09-07', 0),
(8, '2024-09-08', 0),
(9, '2024-09-09', 0),
(10, '2024-09-10', 0),
(11, '2024-09-11', 0),
(12, '2024-09-12', 0),
(13, '2024-09-13', 0),
(14, '2024-09-14', 0),
(15, '2024-09-15', 0),
(16, '2024-09-16', 0),
(17, '2024-09-17', 0),
(18, '2024-09-18', 0),
(19, '2024-09-19', 0),
(20, '2024-09-20', 0),
(1, '2024-09-21', 0),
(2, '2024-09-22', 0),
(3, '2024-09-23', 0),
(4, '2024-09-24', 0),
(5, '2024-09-25', 0),
(6, '2024-09-26', 0),
(7, '2024-09-27', 0),
(8, '2024-09-28', 0),
(9, '2024-09-29', 0),
(10, '2024-09-30', 0),
(11, '2024-10-01', 0),
(12, '2024-10-02', 0),
(13, '2024-10-03', 0),
(14, '2024-10-04', 0),
(15, '2024-10-05', 0),
(16, '2024-10-06', 0),
(17, '2024-10-07', 0),
(18, '2024-10-08', 0),
(19, '2024-10-09', 0),
(20, '2024-10-10', 0);

INSERT INTO detalle_factura (id_factura, id_producto, cantidad, subtotal) VALUES
(1, 1, 1, 750000),
(1, 3, 2, 30000),
(2, 2, 1, 350000),
(2, 5, 10, 12000),
(3, 4, 3, 75000),
(3, 6, 5, 5000),
(4, 7, 2, 50000),
(4, 13, 4, 12000),
(5, 8, 1, 20000),
(5, 10, 2, 24000),
(6, 11, 1, 45000),
(6, 12, 2, 56000),
(7, 14, 1, 20000),
(7, 15, 3, 45000),
(8, 16, 1, 95000),
(9, 17, 5, 40000),
(10, 18, 2, 10000),
(11, 19, 1, 45000),
(12, 20, 1, 400000),
(13, 9, 2, 36000),
-- Factura 21
(21, 2, 1, 350000),
(21, 5, 5, 6000),
-- Factura 22
(22, 3, 3, 45000),
(22, 6, 10, 10000),
-- Factura 23
(23, 1, 1, 750000),
-- Factura 24
(24, 4, 2, 50000),
(24, 9, 1, 18000),
-- Factura 25
(25, 7, 1, 25000),
(25, 13, 5, 15000),
-- Factura 26
(26, 14, 2, 40000),
(26, 20, 1, 400000),
-- Factura 27
(27, 15, 2, 30000),
-- Factura 28
(28, 16, 1, 95000),
(28, 18, 2, 10000),
-- Factura 29
(29, 11, 1, 45000),
(29, 12, 2, 56000),
-- Factura 30
(30, 17, 3, 24000),
(30, 19, 1, 45000),
-- Factura 31
(31, 8, 1, 20000),
(31, 10, 1, 12000),
-- Factura 32
(32, 2, 2, 700000),
-- Factura 33
(33, 6, 20, 20000),
-- Factura 34
(34, 5, 15, 18000),
(34, 9, 1, 18000),
-- Factura 35
(35, 3, 4, 60000),
-- Factura 36
(36, 7, 2, 50000),
(36, 13, 2, 6000),
-- Factura 37
(37, 1, 1, 750000),
(37, 15, 1, 15000),
-- Factura 38
(38, 16, 1, 95000),
-- Factura 39
(39, 20, 1, 400000),
-- Factura 40
(40, 4, 2, 50000),
(40, 6, 3, 3000),
-- Factura 41
(41, 2, 1, 350000),
(41, 10, 2, 24000),
-- Factura 42
(42, 3, 2, 30000),
(42, 11, 1, 45000),
-- Factura 43
(43, 14, 1, 20000),
(43, 17, 3, 24000),
-- Factura 44
(44, 8, 1, 20000),
-- Factura 45
(45, 18, 4, 20000),
(45, 19, 1, 45000),
-- Factura 46
(46, 12, 1, 28000),
(46, 5, 10, 12000),
-- Factura 47
(47, 7, 3, 75000),
-- Factura 48
(48, 13, 6, 18000),
(48, 9, 1, 18000),
-- Factura 49
(49, 15, 2, 30000),
(49, 6, 8, 8000),
-- Factura 50
(50, 20, 1, 400000),
-- Factura 51
(51, 1, 1, 750000),
(51, 3, 2, 30000),
-- Factura 52
(52, 4, 1, 25000),
-- Factura 53
(53, 2, 1, 350000),
(53, 18, 3, 15000),
-- Factura 54
(54, 11, 1, 45000),
-- Factura 55
(55, 16, 1, 95000),
(55, 19, 1, 45000),
-- Factura 56
(56, 12, 2, 56000),
-- Factura 57
(57, 7, 1, 25000),
(57, 9, 1, 18000),
-- Factura 58
(58, 6, 12, 12000),
-- Factura 59
(59, 14, 1, 20000),
(59, 15, 1, 15000),
-- Factura 60
(60, 20, 1, 400000),
(60, 10, 1, 12000);


-- VENTAS TOTALES DE CADA CATEGORIA
SELECT C.nombre_categoria AS Categoria, SUM(D.subtotal) AS Total_ventas
FROM Categorias C JOIN Productos P ON C.id_categoria = P.id_categoria
JOIN detalle_factura D ON P.id_producto = D.id_producto
GROUP BY C.nombre_categoria


-- PROMEDIO VENTAS TOTALES
SELECT AVG(Total_ventas) AS Promedio_ventas
FROM(
	SELECT SUM(D.subtotal) AS Total_ventas
	FROM Categorias C JOIN Productos P ON C.id_categoria = P.id_categoria
	JOIN detalle_factura D ON P.id_producto = D.id_producto
	GROUP BY C.nombre_categoria
)

