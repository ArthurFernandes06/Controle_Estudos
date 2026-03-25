from schemas import SchemaMateria, UserInDB
from repositories import salvar_materia, listar_materias
from seguranca import get_current_user

from fastapi import APIRouter, Depends, status
from typing import Annotated

router = APIRouter()



@router.post("/materias/",status_code=status.HTTP_201_CREATED)
def post_materia(
    materia:SchemaMateria,
    current_user: Annotated[UserInDB, Depends(get_current_user)]
    ):
    materia.user_id = current_user.id
    salvar_materia(materia)
    return {"Mensagem": "Criado"}

@router.get("/materias/",status_code=status.HTTP_200_OK)
async def get_materias(current_user: Annotated[UserInDB, Depends(get_current_user)]):
    materias = listar_materias(user_id=current_user.id)
    return materias

