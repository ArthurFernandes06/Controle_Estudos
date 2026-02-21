from core import connect_db
import uuid

def salvar_user(email: str, senha: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO users (id,email, senha)
            VALUES (?,?, ?)
        """, (id,email, senha))

        connection.commit()