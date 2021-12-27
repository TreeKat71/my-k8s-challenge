import socket

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"


def test_error():
    response = client.get("/error?num=1")
    assert response.status_code == 200
    assert response.json() == {"type": "SyntaxError"}


def test_leave_message():
    visitor = "muller"
    node_name = socket.gethostname()
    response = client.post(
        "/leave_message/",
        json={
            "from_": visitor,
            "content": "DigitalOcean Kubernetes Challenge",
        }
    )
    assert response.status_code == 200
    assert response.json() == f'Hi {visitor}!, you visited {node_name}'
