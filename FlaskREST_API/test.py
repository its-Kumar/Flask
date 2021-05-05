import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 78, "name": "Joe", "views": 1000},
    {"likes": 10002, "name": "How to make REST API", "views": 809994},
    {"likes": 12, "name": "kumar", "views": 200},
]


for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())


# response = requests.get(BASE + "helloworld/chacha/")
# response = requests.put(BASE + 'video/1/', {"data": "data", "name": "testVideo 1"})
# print(response.json())

input()

response = requests.delete(BASE + 'video/2')
print(response)

input()

# response = requests.get(BASE + 'video/2')
# print(response.json())

response = requests.patch(BASE + "video/2", {"views": 122})
print(response.json())


input()

response = requests.get(BASE + 'video/2')
print(response.json())
