from fastapi import APIRouter, status
from schemas.materia import SchemaMateria
from repositories.materia import salvar_materia

router = APIRouter()

@router.post("/materias",status_code=status.HTTP_201_CREATED)
def criar_materia(materia:SchemaMateria):
    salvar_materia(materia.user_id,materia.nome)
    return {"Mensagem": "Criado"}