from ..core import connect_db
from ..schemas import UserInDB
import uuid

def salvar_user(email: str, senha_hash: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO users (id,email, senha)
            VALUES (%s , %s, %s)
        """, (id,email, senha_hash,))

        connection.commit()

def get_user(username: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        cursor.execute("""
        SELECT * FROM users WHERE username = %s
        """,(username,))

        resultado = cursor.fetchall()
        user = UserInDB(id=resultado[id],)
    return user
