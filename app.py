from fastapi import FastAPI
from router.router import libros

app=FastAPI()

app.include_router(libros)
