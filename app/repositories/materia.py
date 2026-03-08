from core import connect_db
from schemas import SchemaMateria

def salvar_materia(materia: SchemaMateria):
    user_id = materia.user_id
    nome = materia.nome
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO materias (user_id, nome)
            VALUES (?, ?)
        """, (user_id, nome))

        connection.commit()

def listar_materias(materia: SchemaMateria):
    user_id = materia.user_id
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, nome from materias 
            WHERE user_id = ?;
        """,(user_id,))

        resultado = cursor.fetchall()

    return resultado