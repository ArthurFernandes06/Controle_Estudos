from pydantic import BaseModel
from typing import Annotated
from fastapi import Path

class SchemaMateria(BaseModel):
    user_id: str
    nome: str

