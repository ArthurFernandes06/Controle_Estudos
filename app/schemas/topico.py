from pydantic import BaseModel
from datetime import datetime
from typing import Annotated
from fastapi import Path

class SchemaTopico(BaseModel):
    id: str
    id_materia: str
    descricao: str | None = None
    nome: str
    prazo: datetime | None = None