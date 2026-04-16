from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import SchemaUser, Token, TokenData
from ..models import ModelUser
from ..security import create_access_token, get_acess_token_expire

ACCESS_TOKEN_EXPIRE_MINUTES = get_acess_token_expire()

router = APIRouter()

@router.post("/cadastro",status_code=status.HTTP_201_CREATED)
def criar_user(user:SchemaUser):
    
    novoUser = ModelUser.criar_user(username=user.username,email=user.email, senha=user.senha)
    return {"Mensagem": "Criado"}



@router.post("/login")
async def login_for_access(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],)-> Token:
    user = ModelUser.autenticar(username=form_data.username,senha=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou Senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")