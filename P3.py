# import sqlite3
# conexion = sqlite3.connect(":memory:")
# conexion.executescript("""
# CREATE TABLE emprendedores(id INTEGER PRIMARY KEY, alias TEXT);
# CREATE TABLE iniciativas(
#     id INTEGER PRIMARY KEY, emprendedor_id INTEGER, estado TEXT
# );
# INSERT INTO emprendedores VALUES
# (1, 'Emprendedor A'), (2, 'Emprendedor B'), (3, 'Emprendedor C');
# INSERT INTO iniciativas VALUES
# (101, 1, 'activa'), (102, 2, 'archivada'), (103, 1, 'activa');
# """)

# consulta = ""  # Completa aquí la consulta solicitada.

# if consulta:
#     print(conexion.execute(consulta).fetchall())

# conexion.close()

# Escribe una consulta que devuelva el identificador de cada iniciativa con estado activa y el alias de su emprendedor 
# responsable, ordenados por identificador de iniciativa. Explica cómo relacionaste las tablas. 
# SQLite es únicamente el recurso del diagnóstico SQL; el curso continuará con MongoDB.

#=========================================================================

import sqlite3

conexion = sqlite3.connect(":memory:") #* Conexion a la base de datos en memoria RAM ":memory:" (No crea ningun archivo en disco)
#ejecutamos un script SQL para crear las tablas y poblarlas con datos de ejemplo
conexion.executescript("""
CREATE TABLE emprendedores (id INTEGER PRIMARY KEY, alias TEXT);
CREATE TABLE iniciativas (
    id INTEGER PRIMARY KEY, 
    emprendedor_id INTEGER, 
    estado TEXT
);

INSERT INTO emprendedores VALUES
(1, 'Emprendedor A'), (2, 'Emprendedor B'), (3, 'Emprendedor C');

INSERT INTO iniciativas VALUES
(101, 1, 'activa'), (102, 2, 'archivada'), (103, 1, 'activa');
""")

consulta = """
SELECT i.id, e.alias
FROM iniciativas i
JOIN emprendedores e ON i.emprendedor_id = e.id
WHERE i.estado = 'activa'
ORDER BY i.id ASC;
"""
# Seleccionamos el id de la iniciativa y el alias del emprendedor con i y e como alias de las tablas, 
# hacemos un JOIN para relacionar las tablas por la clave foránea emprendedor_id y filtramos por estado 'activa', ordenando por id de iniciativa. 

#si la consulta no está vacía (Comparada por defecto), ejecutamos la consulta y mostramos los resultados
if consulta:
    resultados = conexion.execute(consulta).fetchall() #fetchall() hace que se obtengan todos los resultados de la consulta en una lista de tuplas
    print("Resultados de la consulta SQL:", resultados)

conexion.close()

# Explicación de la relación:
# Se realizó un INNER JOIN vinculando el campo de clave foránea `iniciativas.emprendedor_id` 
# con la clave primaria `emprendedores.id`.