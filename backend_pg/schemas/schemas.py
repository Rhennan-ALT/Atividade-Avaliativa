from pydantic import BaseModel, ConfigDict
from typing import Optional

class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False

class TarefaCreate(TarefaBase):
    pass

class TarefaResponse(TarefaBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)