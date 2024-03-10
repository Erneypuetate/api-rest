import psycopg2
from pymongo import MongoClient

# Configuración de la conexión a PostgreSQL
postgres_user = 'user_postgres'
postgres_password = 'password_postgres'
postgres_host = 'localhost'  # Puedes usar una dirección IP o un nombre de host
postgres_port = '5432'  # Cambia si PostgreSQL está configurado en un puerto diferente
postgres_database = 'db_postgres'

# Construir la cadena de conexión
postgres_url = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}'

# Crear una conexión a PostgreSQL
conn = psycopg2.connect(postgres_url)

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Ejemplo de creación de una tabla
create_table_query = '''
CREATE TABLE IF NOT EXISTS libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255),
    autor VARCHAR(255),
    precio NUMERIC
);
'''
cursor.execute(create_table_query)
conn.commit()

# Ejemplo de inserción de datos en PostgreSQL
insert_data_query = '''
INSERT INTO libros (titulo, autor, precio) VALUES
    ('Libro 1', 'Autor 1', 20.50),
    ('Libro 2', 'Autor 2', 18.75),
    ('Libro 3', 'Autor 3', 15.99);
'''
cursor.execute(insert_data_query)
conn.commit()

# Cerrar el cursor y la conexión a PostgreSQL
cursor.close()
conn.close()

# Configuración de la conexión a MongoDB
mongo_user = 'user_mongo'
mongo_password = 'password_mongo'
mongo_host = 'localhost'  # Puedes usar una dirección IP o un nombre de host
mongo_port = 27017
mongo_database = 'db_mongo'

# Crear la cadena de conexión de MongoDB
mongo_url = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_database}'

# Crear un cliente de MongoDB
mongo_client = MongoClient(mongo_url)

# Seleccionar la base de datos
mongo_db = mongo_client[db_mongo]

# Ejemplo de inserción de datos en MongoDB
libros_collection = mongo_db['libros']
libros_collection.insert_many([
    {"titulo": "Libro 1", "autor": "Autor 1", "precio": 20.50},
    {"titulo": "Libro 2", "autor": "Autor 2", "precio": 18.75},
    {"titulo": "Libro 3", "autor": "Autor 3", "precio": 15.99},
])

# Cerrar la conexión a MongoDB
mongo_client.close()
