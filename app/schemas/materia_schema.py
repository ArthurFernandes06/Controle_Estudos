from fastapi import BaseModel

class CreateMateria(BaseModel):
    user_id: int
    nome: str

class GetMateria(BaseModel):
    user_id: int
    nome: str

class DeleteMateria(BaseModel):
    user_id: int
    nome: str