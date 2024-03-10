from pymongo import MongoClient
import time

# Configuración de la conexión a MongoDB
mongo_user = 'user_mongo'
mongo_password = 'password_mongo'
mongo_host = 'localhost'  # Puedes usar una dirección IP o un nombre de host
mongo_port = 27017
mongo_database = 'db_mongo'

# Crear la cadena de conexión de MongoDB
mongo_url = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_database}'
print("URL correcta")

# Crear un cliente de MongoDB
mongo_client = MongoClient(mongo_url)
print("Conexión exitosa")

try:
    # Intenta listar las bases de datos
    database_names = mongo_client.list_database_names()

    # Imprimir las bases de datos
    print("Bases de datos disponibles:")
    for db_name in database_names:
        print(db_name)

except Exception as e:
    # Imprimir el mensaje de error completo
    print(f"Error: {e}")
finally:
    # Cerrar la conexión con MongoDB
    mongo_client.close()
