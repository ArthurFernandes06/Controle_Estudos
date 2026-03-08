from schemas import SchemaMateria
from repositories import salvar_materia, listar_materias

from fastapi import APIRouter,Path, status
from typing import Annotated

router = APIRouter()

@router.post("/materias/{user_id}",status_code=status.HTTP_201_CREATED)
def post_materia(materia:SchemaMateria):
    salvar_materia(materia)
    return {"Mensagem": "Criado"}

@router.get("/materias/{user_id}",status_code=status.HTTP_200_OK)
async def get_materias(user_id: Annotated[str,Path()]):
    materias = listar_materias(user_id=user_id)
    return materias

    