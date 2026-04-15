#app/config.py
# PODATNOSC NR 1:Hardcoded secret key - nigdy nie rob tego w produkcji
#Klucz JWT powinien byc w zmiennej srodowiskowej, nie w kodzie
SECRET_KEY = "super_tajny_klucz_ktory_zna_kazdy_2024"
ALGORITHM = "HS256"
ACCESS_TOKER_EXPIRE_MINUTES = 30

DATABASE_URL = "postgresql://user:password123@localhost:5432/taskdb"
