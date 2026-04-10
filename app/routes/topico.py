
from ..schemas import SchemaTopico, UserInDB
from ..controllers import salvar_topico
from ..security import get_current_user

from typing import Annotated

from fastapi import APIRouter,Depends, status

router = APIRouter()

@router.post("/materias/{materia_id}/topicos/",status_code= status.HTTP_201_CREATED)
def post_topicos(
    materia_id: str,
    topico: SchemaTopico,
    current_user: Annotated[UserInDB, Depends(get_current_user)]
    ):
    topico.materia_id = materia_id
    salvar_topico(topico)
    return {"Mensagem": "Criado"}