import requests

BASE_URL = "http://127.0.0.1:5000"

result = requests.get(BASE_URL + '/ABBV')
print(result.json())

result = requests.put(BASE_URL + '/ABBV', json={"name":"Abbvie Corp."})
print(result.json())
