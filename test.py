import requests

reg = {
    "id": "002",
    "fonte": "esp1",
    "data_status_atual": "28/07/2023 16:20",
    "temperatura": 23.5,    
    "umidade": 79.0,
    "situacao": "ok"
}

headers = {}

response = requests.post("http://192.168.15.10:8000/monitor", json=reg)
print(response)