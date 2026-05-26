# app/main.py

from fastapi import FastAPI
from app.router import users, tasks
from app import models
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Secure CI/CD Pipeline — Task Manager API",
    description="Demo application for security pipeline thesis project",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {
        "message": "Task Manager API is running",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}