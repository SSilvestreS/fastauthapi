from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, database
from app.routes import router as user_router
from app.auth import router as auth_router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Prefixo corrigido para evitar duplicação
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="", tags=["Auth"])  # Removido prefixo duplicado