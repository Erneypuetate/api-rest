import psycopg2
from pymongo import MongoClient

# Parámetros de conexión a PostgreSQL
db_params = {
    'host': 'localhost',
    'database': 'base_de_datos_postgres',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'port': '5432'  # El puerto predeterminado para PostgreSQL es 5432
}

# Conexión a PostgreSQL
try:
    conn = psycopg2.connect(**db_params)
    print("Conexión exitosa a PostgreSQL")

    # Aquí puedes realizar operaciones en la base de datos

except Exception as e:
    print(f"Error de conexión a PostgreSQL: {e}")





# Parámetros de conexión a MongoDB
mongo_params = {
    'host': 'localhost',
    'port': 27017,  # El puerto predeterminado para MongoDB es 27017
    'username': 'tu_usuario',
    'password': 'tu_contraseña',
    'authSource': 'base_de_datos_mongo',
}

# Conexión a MongoDB
try:
    client = MongoClient(**mongo_params)
    db = client.nombre_de_tu_base_de_datos
    print("Conexión exitosa a MongoDB")

    # Aquí puedes realizar operaciones en la base de datos

except Exception as e:
    print(f"Error de conexión a MongoDB: {e}")



