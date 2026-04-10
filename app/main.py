from fastapi import FastAPI
from .routes import router_materia, router_user, router_topico
from .security import router_token

app = FastAPI()

app.include_router(router_materia)
app.include_router(router_user)
app.include_router(router_topico)
app.include_router(router_token)

@app.get("/")
def get_servidor():
    return {"Mensagem": "Servidor Rodando!!"}


