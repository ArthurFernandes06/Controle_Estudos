from pydantic import BaseModel
from typing import Annotated
from fastapi import Path

class SchemaMateria(BaseModel):
    user_id: Annotated[str,Path()]
    nome: str

