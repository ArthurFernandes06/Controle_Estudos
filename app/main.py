from fastapi import FastAPI
from routes import router_materia, router_user


app = FastAPI()
app.include_router(router_materia)
app.include_router(router_user)
@app.get("/")
def get_servidor():
    return {"Mensagem": "Servidor Rodando!!"}


