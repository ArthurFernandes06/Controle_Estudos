from pydantic import BaseModel

class SchemaUser(BaseModel):
    email: str
    senha: str

class UserInDB(BaseModel):
    id: str
    email: str
    senha: str