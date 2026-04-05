from schemas import SchemaMateria, UserInDB
from repositories import salvar_materia, listar_materias
from seguranca import get_current_user

from fastapi import APIRouter,Path, Request, status
from fastapi.responses import HTMLResponse
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

@router.get("/materias/{user_id}",status_code=status.HTTP_200_OK)
async def get_materias(user_id: Annotated[str,Path()]):
    materias = listar_materias(user_id=user_id)
    return materias

