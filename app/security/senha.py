from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()

SENHA_GENIAL = password_hash.hash("senha")

def get_senha_genial():
    return SENHA_GENIAL

def get_password_hash(senha):
    return password_hash.hash(senha)

def verifica_senha(senha_input: str, senha_hashed: str):
    return password_hash.verify(senha_input,senha_hashed)

