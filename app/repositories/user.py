from ..core import connect_db
from psycopg2.extras import RealDictCursor

def salvar_user(id, username, email, senha_hash: str):
    with connect_db() as connection:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO users (id, username, email, senha_hash)
            VALUES (%s ,%s, %s, %s)
        """, (id,username, email, senha_hash,))

        connection.commit()

def get_user(username: str):
    with connect_db() as connection:
        cursor = connection.cursor(cursor_factory=RealDictCursor)

        cursor.execute("""
        SELECT id, username, email, senha_hash FROM users WHERE username = %s
        """,(username,))

        resultado = cursor.fetchone()
        
    return resultado


def listar_materias(user_id: str):
    with connect_db() as connection:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""
            SELECT id, nome from materias 
            WHERE user_id = %s;
        """,(user_id,))

        resultado = cursor.fetchall()

    return resultado