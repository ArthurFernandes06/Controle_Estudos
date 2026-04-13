from ..repositories import get_materia, salvar_materia
import uuid

class ModelMateria:
    def __init__(self, id, id_user, nome):
        self._id = id
        self._user_id = id_user
        self._nome = nome

    @classmethod
    def criar_materia(cls, id_user, nome):
        id = str(uuid.uuid4())
        salvar_materia(id, id_user, nome)
        return cls(id=id, id_user=id_user, nome=nome)

    @classmethod
    def get_materia_from_db(cls, id):
        atributos = get_materia(id)
        id_user = atributos["id_user"]
        nome = atributos["nome"]
        return cls(id=id, id_user=id_user, nome=nome)
    
    @property
    def nome(self):
        return self.__nome

