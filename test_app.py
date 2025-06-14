from app import app


def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, Jenkins CI/CD!'
