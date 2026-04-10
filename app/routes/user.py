from fastapi import APIRouter, status
from ..schemas import SchemaUser
from ..controllers import salvar_user
from ..security import get_password_hash

router = APIRouter()

@router.post("/cadastro",status_code=status.HTTP_201_CREATED)
def criar_user(user:SchemaUser):
    senha_hash = get_password_hash(user.senha)
    salvar_user(user.email, senha_hash)
    return {"Mensagem": "Criado"}
