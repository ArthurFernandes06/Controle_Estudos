import sqlite3
from contextlib import contextmanager

@contextmanager
def connect_db():
    connection = sqlite3.connect("controle_estudos.db")
    connection.execute("PRAGMA foreign_keys = ON;")
    try:
        yield connection
    finally:
        connection.close()