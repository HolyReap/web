import requests

response = requests.post('http://127.0.0.1:5000/advertisements/',
                         json={'title':'ad_1','description':'selling stuff'})
print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:5000/advertisements/1")
print(response.status_code)
print(response.text)

response = requests.patch('http://127.0.0.1:5000/advertisements/1',
                         json={'title':'selling'})
print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:5000/advertisements/1")
print(response.status_code)
print(response.text)

response = requests.patch('http://127.0.0.1:5000/advertisements/2',
                         json={'title':'selling'})
print(response.status_code)
print(response.text)

response = requests.post('http://127.0.0.1:5000/advertisements/',
                         json={'title':'to long of a title to post as an advertisement_____________','description':'selling other stuff'})
print(response.status_code)
print(response.text)

response = requests.delete('http://127.0.0.1:5000/advertisements/1')
print(response.status_code)
print(response.text)