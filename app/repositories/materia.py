from ..core import connect_db

def salvar_materia(id,user_id, nome):
    
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO materias (id,id_user, nome)
            VALUES (%s , %s, %s)
        """, (id, user_id, nome,))

        connection.commit()

def get_materia(id):
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT (id, id_user, nome) WHERE id = %s;
        """,(id,))

        resultado = cursor.fetchall()
    
    return resultado



def atualizar_materias(id, nome):
    with connect_db as connection:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE nome = %s WHERE id = %s;
        """,(nome, id,))

        connection.commit()

def deletar_materia(materia_id):
    pass

def listar_topicos():
    pass