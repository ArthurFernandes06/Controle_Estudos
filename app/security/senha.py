from pwdlib import PasswordHash
from ..controllers import get_user
password_hash = PasswordHash.recommended()

SENHA_GENIAL = password_hash.hash("senha")

def get_password_hash(senha):
    return password_hash.hash(senha)

def verifica_senha(senha_input: str, senha_hashed: str):
    return password_hash.verify(senha_input,senha_hashed)

def autenticar_user(email: str, senha: str):
    user = get_user(email)
    if not user:
        verifica_senha(senha, SENHA_GENIAL)
        return False
    if not verifica_senha(senha, user.senha):
        return False
    return user