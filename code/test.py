import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

def test_put_stock_code_201(): 
    result = requests.put(BASE_URL + '/ABBV', json={"name":"Abbvie Corp."})
    assert result.status_code == 201

def test_get_stock_code_200():
    result = requests.get(BASE_URL + '/ABBV')
    assert result.status_code == 200

def test_delete_stock_code_200():
    result = requests.delete(BASE_URL + '/ABBV')
    assert result.status_code == 200
