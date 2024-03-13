from pymongo import MongoClient

# Configuración de la conexión a MongoDB
mongo_user = 'user_mongo'
mongo_password = 'password_mongo'
mongo_host = 'localhost'  # Puedes usar una dirección IP o un nombre de host
mongo_port = 27017
mongo_database = 'db_mongo'

# Crear la cadena de conexión de MongoDB
mongo_url = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}'

# Crear un cliente de MongoDB
mongo_client = MongoClient(mongo_url)
    
# Seleccionar la base de datos
mongo_db = mongo_client["malate"]

# Ejemplo de inserción de datos en MongoDB
libros_collection = mongo_db['libros']
libros_collection.insert_many([
    {"titulo": "Libro 1", "autor": "Autor 1", "precio": 20.50},
    {"titulo": "Libro 2", "autor": "Autor 2", "precio": 18.75},
    {"titulo": "Libro 3", "autor": "Autor 3", "precio": 15.99},
])

# Cerrar la conexión a MongoDB
mongo_client.close()
