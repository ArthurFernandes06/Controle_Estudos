from pydantic import BaseModel
from datetime import datetime

class SchemaSessoes(BaseModel):
    topico_id: int
    duracao: int
    dt_inicio: datetime
    dt_fim: datetime | None = None