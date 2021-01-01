import requests
import pytest
import json
from os import environ

APP_HOST = environ["APP_HOST"] if "APP_HOST" in environ else "localhost"
APP_PORT = environ["APP_PORT"] if "APP_PORT" in environ else "5000"

BASE_URL = "http://" + APP_HOST + ":" + APP_PORT

def test_get_stock_code_404():
    result = requests.get(BASE_URL + '/ABBV')
    assert result.status_code == 404

def test_put_stock_code_201(): 
    result = requests.put(BASE_URL + '/ABBV', json={"name":"Abbvie Corp."})
    assert result.status_code == 201

def test_get_stock_code_200_and_text():
    result = requests.get(BASE_URL + '/ABBV')
    assert result.status_code == 200
    assert json.loads(result.text) == {"id":"ABBV","name":"Abbvie Corp."}

def test_post_stock_code_204():
    result = requests.post(BASE_URL + '/ABBV', json={"name":"Abbvie Corporation"})
    assert result.status_code == 204


def test_get_stock_code_200_and_text_after_update():
    result = requests.get(BASE_URL + '/ABBV')
    assert result.status_code == 200
    assert json.loads(result.text) == {"id":"ABBV","name":"Abbvie Corporation"}

def test_delete_stock_code_200():
    result = requests.delete(BASE_URL + '/ABBV')
    assert result.status_code == 200
