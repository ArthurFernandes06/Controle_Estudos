from pydantic import BaseModel

class SchemaUser(BaseModel):
    id: str
    username: str
    email: str
    senha: str

class UserInDB(BaseModel):
    id: str
    email: str
    senha: str