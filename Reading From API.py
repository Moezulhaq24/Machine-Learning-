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

# Storing data in the list
for datum in data:
    ids.append(datum['id'])
    emails.append(datum['email'])

# Printing only the id's and email of the persons from the data
# for id in ids:
#     print(id)

# for email in emails:
#     print(email)


# Printing the email and id of a person side by side from a website using api 
for email,id in zip(emails,ids):
    print(f"ID: {id}, Email: {email}")