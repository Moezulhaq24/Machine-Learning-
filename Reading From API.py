import requests
import json

url = "https://reqres.in/"

response = requests.get(url+"/api/users?page=2").json()


# print(response)

data = response["data"]

# Printing the specific data from website using API
# for datum in data:
#     print(datum)

ids = []
emails = []

# Printing only the id's and email of the persons from the data
for datum in data:
    ids.append(datum['id'])
    emails.append(datum['email'])

for id in ids:
    print(id)

for email in emails:
    print(email)

