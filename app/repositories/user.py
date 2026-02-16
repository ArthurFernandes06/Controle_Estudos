from core import connect_db

def salvar_user(email: str, senha: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            );
        """)

        cursor.execute("""
            INSERT INTO users (email, senha)
            VALUES (?, ?)
        """, (email, senha))

        connection.commit()