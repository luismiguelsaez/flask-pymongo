import requests
import pytest
import json

BASE_URL = "http://127.0.0.1:5000"

def test_put_stock_code_201(): 
    result = requests.put(BASE_URL + '/ABBV', json={"name":"Abbvie Corp."})
    assert result.status_code == 201

def test_get_stock_code_200_and_text():
    result = requests.get(BASE_URL + '/ABBV')
    assert result.status_code == 200
    assert json.loads(result.text) == {"name":"Abbvie Corp."}

def test_post_stock_code_204():
    result = requests.post(BASE_URL + '/ABBV', json={"name":"Abbvie Corporation"})
    assert result.status_code == 204


def test_get_stock_code_200_and_text_after_update():
    result = requests.get(BASE_URL + '/ABBV')
    assert result.status_code == 200
    assert json.loads(result.text) == {"name":"Abbvie Corporation"}

def test_delete_stock_code_200():
    result = requests.delete(BASE_URL + '/ABBV')
    assert result.status_code == 200
