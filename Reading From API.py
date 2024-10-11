import requests
import json

url = "https://reqres.in/"

response = requests.get(url+"/api/users?page=2").json()


# print(response)

data = response["data"]

for datum in data:
    print(datum)
