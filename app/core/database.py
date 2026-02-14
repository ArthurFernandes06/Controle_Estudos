import sqlite3
import os
from contextlib import contextmanager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../../"))
DB_PATH = os.path.join(PROJECT_ROOT,"controle_estudos.db")

@contextmanager
def connect_db():
    connection = sqlite3.connect(DB_PATH)
    connection.execute("PRAGMA foreign_keys = ON;")
    try:
        yield connection
    finally:
        connection.close()

if __name__ == "__main__":
    with connect_db() as connection:
        cursor = connection.cursor()

        #Criação de cliente
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            );
        """)

        #Criação de matérias
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS materias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                FOREIGN KEY(user_id) references users(id) ON DELETE CASCADE
            );
        """)

        #Criação de Tópicos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS  topicos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                materia_id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                prazo TEXT,
                FOREIGN KEY(materia_id) REFERENCES materias(id) ON DELETE CASCADE
            );
        """)

        #Criação do registro de estudo
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessao_estudos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topico_id INTEGER NOT NULL,
                duracao_minutos INTEGER,
                inicio TEXT DEFAULT(datetime('now')),
                fim TEXT, 
                FOREIGN KEY(topico_id) REFERENCES topicos(id) ON DELETE CASCADE
            );
        """)
        connection.commit()