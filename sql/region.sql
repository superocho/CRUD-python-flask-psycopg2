DROP TABLE IF EXISTS region_cl CASCADE;
CREATE TABLE region_cl (
  id_re INT NOT NULL PRIMARY KEY, 	-- ID unico
  str_descripcion varchar(60) NOT NULL, -- Nombre extenso
  str_romano varchar(5) NOT NULL, 	-- Numero de region
  num_provincias INT NOT NULL, 		-- Total de provincias
  num_comunas INT NOT NULL 		-- Total de comunas
);
--LOCK TABLE region_cl IN EXCLUSIVE MODE;

INSERT INTO region_cl VALUES
(1,'DE ARICA Y PARINACOTA','XV',2,4),
(2,'DE TARAPACÁ','I',2,7),
(3,'DE ANTOFAGASTA','II',3,9),
(4,'DE ATACAMA','III',3,9),
(5,'DE COQUIMBO','IV',3,15),
(6,'DE VALPARAÍSO','V',8,38),
(7,'DEL LIBERTADOR GRAL. BERNARDO O''HIGGINS','VI',3,33),
(8,'DEL MAULE','VII',4,30),
(9,'DE ÑUBLE','XVI',3,21),
(10,'DEL BIOBÍO ','VIII',3,33),
(11,'DE LA ARAUCANÍA','IX',2,32),
(12,'DE LOS RÍOS','XIV',2,12),
(13,'DE LOS LAGOS','X',4,30),
(14,'DE AYSÉN DEL GRAL. CARLOS IBAÑEZ DEL CAMPO ','XI',4,10),
(15,'DE MAGALLANES Y DE LA ANTÁRTICA CHILENA','XII',4,11),
(16,'METROPOLITANA DE SANTIAGO','RM',6,52);
