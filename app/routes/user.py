from fastapi import APIRouter, status
from schemas import SchemaUser
from repositories import salvar_user

router = APIRouter()

@router.post("/user",status_code=status.HTTP_201_CREATED)
def criar_user(user:SchemaUser):
    salvar_user(user.email,user.senha)
    return {"Mensagem": "Criado"}