from sqlalchemy import Table, Column, Integer, String
from config.db import engine_postgres, meta_data_postgres

# Cambia 'table' a 'Table', 'true' a 'True' y agrega comas después de cada columna
books = Table("books", meta_data_postgres,
              Column("id", Integer, primary_key=True),
              Column("name", String),
              Column("presio", Integer))

# Cambia 'meta_data_postgres' a 'meta_data_postgres' (que se importa desde 'config.db')
meta_data_postgres.create_all(engine_postgres)
