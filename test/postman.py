import requests

url = "http://0.0.0.0:8080/useradd"

payload = {
    "name": "Bob",
    "age": 27,
    "city": "Oakland"
}
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "5b192169-7157-4585-a852-111ccfc2f287"
}

response = requests.request("POST", url, data=str(payload), headers=headers)

print(response.text)
