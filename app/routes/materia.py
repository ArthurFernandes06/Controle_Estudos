from schemas import SchemaMateria
from repositories import salvar_materia, listar_materias

from fastapi import APIRouter,Path, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated

router = APIRouter()
templates = Jinja2Templates(directory="templates/materia")


@router.post("/materias/{user_id}",status_code=status.HTTP_201_CREATED)
def post_materia(materia:SchemaMateria):
    salvar_materia(materia)
    return {"Mensagem": "Criado"}

@router.get("/api/materias/{user_id}",status_code=status.HTTP_200_OK)
async def get_materias(user_id: Annotated[str,Path()]):
    materias = listar_materias(user_id=user_id)
    return materias

@router.get("/views/materias/{user_id}",response_class=HTMLResponse)
def get_html(request: Request, user_id: str):
    return templates.TemplateResponse(request=request, name="materia.html")