# app/config.py
import os

# PODATNOSC NR 1: Hardcoded secret key jako fallback
# W produkcji SECRET_KEY powinien byc TYLKO w zmiennej srodowiskowej
SECRET_KEY = os.getenv("SECRET_KEY", "super_tajny_klucz_ktory_zna_kazdy_2024")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password123@localhost:5432/taskdb"
)