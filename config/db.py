import psycopg2
from pymongo import MongoClient

# Configuración de la conexión a PostgreSQL
postgres_user = 'user_postgres'
postgres_password = 'password_postgres'
postgres_host = 'localhost'  
postgres_port = '5432'  
postgres_database = 'db_postgres'

# Construir la cadena de conexión
postgres_url = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}'

# Crear una conexión a PostgreSQL
conn_postgres = psycopg2.connect(postgres_url)

# Configuración de la conexión a MongoDB
mongo_user = 'user_mongo'
mongo_password = 'password_mongo'
mongo_host = 'localhost'  
mongo_port = 27017
mongo_database = 'db_mongo'

# Crear la cadena de conexión de MongoDB
mongo_url = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}'

# Crear un cliente de MongoDB
conn_mongo = MongoClient(mongo_url)
