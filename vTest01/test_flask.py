import requests

r = requests.get(
    'http://127.0.0.1:5000/employee/jun'
)
print(r.text)

r = requests.post(
    'http://127.0.0.1:5000/employee', data={'username': 'jun'}
)
print(r.text)

r = requests.put(
    'http://127.0.0.1:5000/employee', data={'username': 'jun'}
)
print(r.text)

r = requests.delete(
    'http://127.0.0.1:5000/employee', data={'username': 'jun'}
)
print(r.text)