from pydantic import BaseModel
from datetime import datetime
from typing import Annotated
from fastapi import Path

class SchemaTopico(BaseModel):
    materia_id: Annotated[int,Path()]
    nome: str
    prazo: datetime | None = None