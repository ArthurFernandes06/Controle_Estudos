from fastapi import APIRouter, status
from schemas.materia_schema import CreateMateria
from repositories.materia_repositorie import salvar_materia

router = APIRouter()

@router.post("/materias")
def criar_materia(materia:CreateMateria,status_code=status.HTTP_201_CREATED):
    salvar_materia(materia.user_id,materia.nome)
    return {"Mensagem": "Criado"}