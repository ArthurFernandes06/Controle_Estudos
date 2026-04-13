from ..core import connect_db
import uuid

def salvar_topico(id_materia, nome,descricao, prazo):
    id = str(uuid.uuid4())
    
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO topicos (id, id_materia, nome, descricao, prazo)
            VALUES(%s , %s, %s);
            """,(id, id_materia, nome, descricao, prazo,))
        
        connection.commit()


def atualizar_topico():
    pass

def deletar_topico():
    pass