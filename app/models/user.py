from ..repositories import get_user, salvar_user
from ..security import verifica_senha, get_password_hash,get_senha_genial
import uuid

SENHA_GENIAL = get_senha_genial()

class ModelUser:
    
    def __init__(self, id, username, email, senha_hash):
        self._id = id
        self._username = username
        self._email = email
        self._senha_hash = senha_hash

    @property
    def username(self):
        return self._username

    @classmethod
    def criar_user(cls, username, email, senha):
        id = str(uuid.uuid4())
        senha_hash = get_password_hash(senha)
        salvar_user(id, username, email, senha_hash)
        return cls(id=id,username=username, email=email,senha_hash=senha_hash)

    @classmethod
    def get_user_db(cls,username):
        try:
            atributos = get_user(username)
            id = atributos["id"]
            email = atributos["email"]
            senha_hash = atributos["senha_hash"]
        except AttributeError:
            return None
        return cls(id=id, username=username, email=email, senha_hash=senha_hash)

    @classmethod
    def autenticar(cls,username, senha):
        try:
            atributos = get_user(username)
            id = atributos["id"]
            email = atributos["email"]
            senha_hash = atributos["senha_hash"]

            if verifica_senha(senha_input=senha, senha_hashed=senha_hash):
                return cls(id=id, username=username, email=email, senha_hash=senha_hash)
            return None
        
        except AttributeError:
            verifica_senha(senha_input=senha, senha_hashed=SENHA_GENIAL)
            return None
        
        
        
    
