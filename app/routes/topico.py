from schemas import SchemaTopico
from repositories import salvar_topico
from fastapi import APIRouter, status

router = APIRouter()

@router.post("/topicos/{materia_id}",status_code= status.HTTP_201_CREATED)
def post_topicos(topico: SchemaTopico):
    salvar_topico(topico)
    return {"Mensagem": "Criado"}