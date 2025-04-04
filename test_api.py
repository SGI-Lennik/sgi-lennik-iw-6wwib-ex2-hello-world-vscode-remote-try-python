import pytest
import json
from app import app

def test_get_all_books():
    response = app.test_client().get('/bookapi/books')
    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Harvard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list

def test_get_book_by_id():
    response = app.test_client().get('/bookapi/books/1')
    res = json.loads(response.data.decode('utf-8')).get("Book")
    print(res)
    assert res['id'] == 1
    assert res['author'] == 'Harvard'
    assert res['title'] == 'CS50'
    assert response.status_code == 200
