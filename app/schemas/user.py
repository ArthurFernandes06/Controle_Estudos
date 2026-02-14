from pydantic import BaseModel

class SchemaUser(BaseModel):
    email: str
    senha: str
