# tests/test_main.py

from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    with patch("app.database.engine"):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200