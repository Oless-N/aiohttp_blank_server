import time

import requests
import json

url = "http://0.0.0.0:8080/usersinfo"

payload = {"name": "Bob",
           "age": 27,
           "city": "Oakland"
           }
headers = {'Content-Type': "application/json"}
data = json.dumps(payload)
done = True
if __name__ == '__main__':
    while (done):
        print('POST', data)
        t = time.time()
        response = requests.request("POST", url, data=data, headers=headers)
        print('time of response', time.time() - t)
        print(response.text)
        done = False
