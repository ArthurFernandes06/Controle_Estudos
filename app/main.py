from fastapi import FastAPI
from routes.materia import router as router_materia
from routes.user import router as router_user

app = FastAPI()
app.include_router(router_materia)
app.include_router(router_user)
@app.get("/")
def get_servidor():
    return {"Mensagem": "Servidor Rodando!!"}


