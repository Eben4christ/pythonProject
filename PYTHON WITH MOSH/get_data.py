import requests
res = requests.get('http://127.0.0.1:5000/data/1')
if res.ok:
    print(res.json())