# Etap 1: Builder — instalujemy zależności
FROM python:3.13-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt


# Etap 2: Runtime — minimalny obraz produkcyjny
FROM python:3.13-slim AS runtime

# PODATNOSC NR 4: Kontener uruchomiony jako root!
# Nigdy nie uruchamiaj kontenera produkcyjnego jako root.
# Checkov wykryje brak instrukcji USER i oznaczy to jako blad.
# Poprawka: dodac przed CMD linie:
# RUN useradd -m appuser
# USER appuser

WORKDIR /app

# Kopiujemy zainstalowane biblioteki z etapu builder
COPY --from=builder /root/.local /root/.local

# Kopiujemy kod aplikacji
COPY app/ ./app/

# Ustawiamy zmienne srodowiskowe
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Port na ktorym dziala aplikacja
EXPOSE 8000

# Komenda uruchamiajaca aplikacje
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]