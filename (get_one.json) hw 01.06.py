import json
import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)
# json_data = response.content.decode()
# print(json_data)
# with open('get_one.json', 'w') as file:
#     json.dump(get_one.json, file)

url = "https://api.instantwebtools.net/v1/airlines"
response = requests.get(url)
json_data = response.content.decode()
print(json_data)
for i in range(0,10):
    with open(f'{i}get_one.json', 'w') as file:
        json.dump(json_data, file)
