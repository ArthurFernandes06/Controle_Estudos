from ..core import connect_db
from ..schemas import SchemaMateria
import uuid


def salvar_materia(materia: SchemaMateria):
    id = str(uuid.uuid4())
    user_id = materia.user_id
    nome = materia.nome
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO materias (id,user_id, nome)
            VALUES (%s , %s, %s)
        """, (id, user_id, nome,))

        connection.commit()

def listar_materias(user_id: str):
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT id, nome from materias 
            WHERE user_id = %s;
        """,(user_id,))

        resultado = cursor.fetchall()

    return resultado


def atualizar_materias(materia: SchemaMateria):
    with connect_db as connection:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE nome = %s WHERE id = %s;
        """,(materia.nome, materia.id,))

        connection.commit()

def deletar_materia(materia_id):
    with connect_db as connection:
        pass