# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
import hashlib
from app.database import get_db
from app import models
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# PODATNOSC NR 2: Slabe hashowanie hasel - MD5 jest zlamany od lat!
# Nalezy uzywac bcrypt lub argon2
def hash_password_weak(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(
        models.User.username == user.username
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed = hash_password_weak(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created", "id": new_user.id}


# PODATNOSC NR 3: SQL Injection - nigdy nie wstawiaj danych uzytkownika
# bezposrednio do zapytania SQL!
@router.get("/search")
def search_users(username: str, db: Session = Depends(get_db)):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = db.execute(text(query))
    users = result.fetchall()
    return {"users": [dict(row._mapping) for row in users]}