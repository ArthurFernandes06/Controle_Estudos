from core.database import connect_db

def salvar_materia(user_id: int, nome: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS materias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                nome TEXT NOT NULL,
                FOREIGN KEY(user_id) references users(id)
            );
        """)

        cursor.execute("""
            INSERT INTO materias (user_id, nome)
            VALUES (?, ?)
        """, (user_id, nome))

        connection.commit()