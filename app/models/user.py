from ..repositories import get_user, salvar_user
from ..security import verifica_senha, get_senha_genial, get_password_hash
import uuid



class ModelUser:
    
    def __init__(self, id, username, email, senha_hash):
        self._id = id
        self._username = username
        self._email = email
        self._senha_hash = senha_hash

    @classmethod
    def criar_user(cls, username, email, senha):
        id = str(uuid.uuid4())
        senha_hash = get_password_hash(senha)
        salvar_user(id, username, email, senha_hash)
        return cls(id=id,username=username, email=email,senha_hash=senha_hash)

    @classmethod
    def get_user_db(cls,username):
        atributos = get_user(username)
        id = atributos["id"]
        email = atributos["email"]
        senha_hash = atributos["senha_hash"]
        return cls(id=id, username=username, email=email, senha_hash=senha_hash)

    def autenticar(self,senha):
        if not verifica_senha(senha_input=senha, senha_hashed=self._senha_hash):
            return False
        return True