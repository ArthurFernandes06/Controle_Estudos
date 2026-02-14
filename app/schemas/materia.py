from pydantic import BaseModel

class SchemaMateria(BaseModel):
    user_id: int
    nome: str

