from sqlalchemy import create_engine, MetaData

# Configuración de la conexión a PostgreSQL
postgres_user = 'user_postgres'
postgres_password = 'password_postgres'
postgres_host = 'localhost'
postgres_port = '5432'
postgres_database = 'db_postgres'

# Construir la cadena de conexión
postgres_url = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}'

# Crear el motor de SQLAlchemy
engine_postgres = create_engine(postgres_url)
meta_data_postgres = MetaData()