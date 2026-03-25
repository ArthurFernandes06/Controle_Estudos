from repositories import get_user
from seguranca import get_password_hash, autenticar_user

print("Autenticação:")
print(autenticar_user("email@email.com", "1234"))
print(autenticar_user("arthur@email.com", "senha"))
