from core.database import connect_db

def salvar_materia(user_id: int, nome: str):
    with connect_db() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO materias 
                           (user_id,nome) 
                            VALUES(%s,%s)""",
                           (user_id,nome)
            )
        connection.commit()