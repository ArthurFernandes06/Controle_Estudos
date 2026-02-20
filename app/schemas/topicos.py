from pydantic import BaseModel
from datetime import datetime

class SchemaTopicos(BaseModel):
    materia_id: int
    nome: str
    prazo: datetime | None = None