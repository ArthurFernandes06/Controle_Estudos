from ..core import connect_db
from ..schemas import SchemaTopico
import uuid

def salvar_topico(topico: SchemaTopico):
    id = str(uuid.uuid4())
    materia_id = topico.materia_id
    nome =  topico.nome
    prazo = topico.prazo
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO topicos (id,materia_id,nome,prazo)
            VALUES(?,?,?);
            """,(id, materia_id,nome,prazo,))
        
        connection.commit()

def get_topicos():
    pass

def atualizar_topico():
    pass

def deletar_topico():
    pass