from core import connect_db

def salvar_materia(user_id: int, nome: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO materias (user_id, nome)
            VALUES (?, ?)
        """, (user_id, nome))

        connection.commit()

def listar_materias(user_id: int):
    with connect_db() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, nome from materias 
            WHERE user_id = ?;
        """,(user_id,))

        resultado = cursor.fetchall()

    return resultado