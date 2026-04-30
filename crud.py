from sqlalchemy.orm import Session
from backend_pg.models.models import Tarefa
from backend_pg.schemas.schemas import TarefaCreate

def listar_tarefas(db: Session):
    return db.query(Tarefa).all()

def buscar_tarefa(db: Session, tarefa_id: int):
    return db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

def criar_tarefa(db: Session, tarefa: TarefaCreate):
    nova_tarefa = Tarefa(**tarefa.model_dump())
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

def atualizar_tarefa(db: Session, tarefa_id: int, dados: TarefaCreate):
    tarefa = buscar_tarefa(db, tarefa_id)
    if tarefa:
        for chave, valor in dados.model_dump().items():
            setattr(tarefa, chave, valor)
        db.commit()
        db.refresh(tarefa)
    return tarefa

def deletar_tarefa(db: Session, tarefa_id: int):
    tarefa = buscar_tarefa(db, tarefa_id)
    if tarefa:
        db.delete(tarefa)
        db.commit()
    return tarefa

def concluir_tarefa_db(db: Session, tarefa_id: int):
    tarefa = buscar_tarefa(db, tarefa_id)
    if tarefa:
        tarefa.concluida = not tarefa.concluida 
        db.commit()
        db.refresh(tarefa)
    return tarefa