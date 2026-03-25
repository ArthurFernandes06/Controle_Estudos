from core import connect_db
from schemas import UserInDB
import uuid

def salvar_user(email: str, senha_hash: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        id = str(uuid.uuid4())
        cursor.execute("""
            INSERT INTO users (id,email, senha)
            VALUES (?,?, ?);
        """, (id,email, senha_hash,))

        connection.commit()

def get_user(email: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        cursor.execute("""
        SELECT id, email, senha FROM users WHERE email = ?;
        """,(email,))

        resultado = cursor.fetchone()

        if resultado:
            return UserInDB(
                id=resultado[0],
                email=resultado[1],
                senha=resultado[2]
            )

        return None