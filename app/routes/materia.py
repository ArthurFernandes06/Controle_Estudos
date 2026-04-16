from ..schemas import SchemaMateria, UserInDB
from ..models import ModelMateria
from ..security import get_current_user

from fastapi import APIRouter, Depends,Path, Request, status
from fastapi.responses import HTMLResponse
from typing import Annotated

router = APIRouter()



@router.post("/materias/",status_code=status.HTTP_201_CREATED)
def post_materia(
    materia:SchemaMateria,
    current_user: Annotated[UserInDB, Depends(get_current_user)]
    ):
    materia.user_id = current_user.id
    return {"Mensagem": "Criado"}


