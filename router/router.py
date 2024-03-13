from fastapi import APIRouter
from model.tablas import Books
from config.db import conn_postgres, postgres_url
import pandas as pd
from sqlalchemy import create_engine
import json

libros=APIRouter()

@libros.get("/libros")
def listar_libros():
    try:
        with conn_postgres.cursor() as cursor:
            query = 'SELECT * FROM books;'
            cursor.execute(query)
            records = cursor.fetchall()

            column_names = [desc[0] for desc in cursor.description]
            resultados_dict = [dict(zip(column_names, record)) for record in records]
            

        return resultados_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
@libros.post("/registrar")
def registrar_libro(libro: Books):
    nuevo_libro=pd.DataFrame(libro).transpose()
    nuevo_libro.columns = nuevo_libro.iloc[0]
    nuevo_libro = nuevo_libro[1:]
    engine=create_engine(postgres_url)
    nuevo_libro.to_sql('books', engine, if_exists='append', index=False)
    print(nuevo_libro)
    return "registro exitoso"