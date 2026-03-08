from core import connect_db
from schemas import SchemaTopico

def salvar_topico(topico: SchemaTopico):
    materia_id = topico.materia_id
    nome =  topico.nome
    prazo = topico.prazo
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO topicos (materia_id,nome,prazo)
            VALUES(?,?,?);
            """,(materia_id,nome,prazo,))
        
        connection.commit()