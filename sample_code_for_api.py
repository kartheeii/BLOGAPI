import requests

url = "https://kartheee.pythonanywhere.com/api/"
response = requests.get(url)

print("Status Code:", response.status_code)
print(response.json())


import requests

url = "https://kartheee.pythonanywhere.com/api/"
data = {
    "title": "New Blog Post",
    "content": "This is the content of the new post."
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print(response.json())





