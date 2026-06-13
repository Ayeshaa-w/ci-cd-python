import pytest
from app import app
@pytest.fixture
def client():
    app.config['TESTING']=True
    with app.test_client() as client:
        yield client
def test_create_item(client):
    res=client.post('/items',json={'name':'laptop'})
    assert res.status_code==201
    assert res.get_json()['name']=='laptop'
def test_get_items(client):
    client.post('/items', json={'name': 'phone'})
    res = client.get('/items')
    assert res.status_code == 200
    assert len(res.get_json()) >= 1

def test_get_single_item(client):
    client.post('/items', json={'name': 'tablet'})
    res = client.get('/items/1')
    assert res.status_code == 200

def test_delete_item(client):
    client.post('/items', json={'name': 'mouse'})
    res = client.delete('/items/1')
    assert res.status_code == 200

def test_missing_field(client):
    res = client.post('/items', json={})
    assert res.status_code == 400

def test_not_found(client):
    res = client.get('/items/999')
    assert res.status_code == 404
