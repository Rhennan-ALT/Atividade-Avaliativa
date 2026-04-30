from fastapi import FastAPI
from database import engine, Base
from backend_pg.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gerenciador de Tarefas")

app.include_router(router.router)