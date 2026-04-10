from contextlib import contextmanager
import psycopg2
import os

@contextmanager
def connect_db():
    connection = psycopg2.connect(
        host= os.getenv("HOST_DB"),          
        database= os.getenv("POSTGRES_DB"),
        user= os.getenv("APP_DB_USER"),
        password= os.getenv("APP_DB_PASSWORD")
    )
    
    try:
        yield connection

    finally:
        connection.close()

print(os.getenv("DB_HOST"))
print(os.getenv("POSTGRES_DB"))