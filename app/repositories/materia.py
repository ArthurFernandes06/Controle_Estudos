from core import connect_db

def salvar_materia(user_id: int, nome: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        

        cursor.execute("""
            INSERT INTO materias (user_id, nome)
            VALUES (?, ?)
        """, (user_id, nome))

        connection.commit()