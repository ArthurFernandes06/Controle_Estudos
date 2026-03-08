from fastapi import FastAPI
from routes import router_materia, router_user, router_topico


app = FastAPI()
app.include_router(router_materia)
app.include_router(router_user)
app.include_router(router_topico)
@app.get("/")
def get_servidor():
    return {"Mensagem": "Servidor Rodando!!"}


