from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import crud
from backend_pg.schemas.schemas import TarefaCreate, TarefaResponse

router = APIRouter(prefix="/tarefas", tags=["Tarefas"])

@router.post("/", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED)
def criar(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    return crud.criar_tarefa(db, tarefa)

@router.get("/", response_model=list[TarefaResponse])
def listar(db: Session = Depends(get_db)):
    return crud.listar_tarefas(db)

@router.get("/{tarefa_id}", response_model=TarefaResponse)
def buscar(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = crud.buscar_tarefa(db, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@router.put("/{tarefa_id}", response_model=TarefaResponse)
def atualizar(tarefa_id: int, dados: TarefaCreate, db: Session = Depends(get_db)):
    tarefa = crud.atualizar_tarefa(db, tarefa_id, dados)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@router.delete("/{tarefa_id}")
def deletar(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = crud.deletar_tarefa(db, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"msg": "Deletado com sucesso"}

@router.patch("/{tarefa_id}/concluir", response_model=TarefaResponse)
def concluir_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = crud.concluir_tarefa_db(db, tarefa_id)
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa