
import pytest

# https://pytest-with-eric.com/pytest-advanced/pytest-fastapi-testing/

@pytest.mark.skip(reason="no way of currently testing this")
def test_skip():
    assert 1 != 1
    
    
def test_api(mock_client):
    response = mock_client.get("/")
    assert response is not None
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
    
def test_CRUD_api(mock_client):
    sample_payload = {
        "title": "test_title",
        "description": "test_decription",
        "completed": "False"
    }
    
    # Create Item
    response = mock_client.post("/es/searcj", json=sample_payload)
    assert response.status_code == 200
    # assert response.json() == {
    #     "message ": "OK - Successful Query executed",
    #     "uuid": response.json()['uuid']
    # }
    
    
    