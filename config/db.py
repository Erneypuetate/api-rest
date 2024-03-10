from sqlalchemy import create_engine, MetaData

# Configuración de la conexión a PostgreSQL
postgres_user = 'user_postgre'
postgres_password = 'password_postgres'
postgres_host = 'postgres'
postgres_port = '5432'
postgres_database = 'db_postgres'

# Construir la cadena de conexión
postgres_url = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}'

# Crear el motor de SQLAlchemy
engine = create_engine(postgres_url)




# Configuración de la conexión a MongoDB
mongo_user = 'user_mongo'
mongo_password = 'password_mongo'
mongo_host = 'mongo'
mongo_port = '27017'
mongo_database = 'db_mongo'

# Construir la cadena de conexión
mongo_url = f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_database}'

# Crear el motor de SQLAlchemy
engine = create_engine(mongo_url)

# Crear un objeto Metadata para manejar la estructura de la base de datos
metadata = MetaData()



