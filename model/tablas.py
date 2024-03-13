import psycopg2
from config.db import conn_postgres
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Books(BaseModel):
    id: Optional[int]  # PRIMARY KEY
    titulo: str
    autor_nombre: str
    autor_nacionalidad: str
    autor_fecha_nacimiento: date
    autor_genero: str
    nombre_editorial: str
    ubicacion_editorial: str
    isbn: float
    precio: float
    cantidad_stock: int


# Crear un cursor para ejecutar consultas SQL
cursor = conn_postgres.cursor()

# Ejemplo de creación de una tabla
create_table_query = '''
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    autor_nombre VARCHAR(255),
    autor_nacionalidad VARCHAR(255),
    autor_fecha_nacimiento DATE,
    autor_genero VARCHAR(255),
    nombre_editorial VARCHAR(255),
    ubicacion_editorial VARCHAR(255),
    isbn FLOAT,
    precio FLOAT,
    cantidad_stock INTEGER
);
'''
cursor.execute(create_table_query)
conn_postgres.commit()


cursor.close()

