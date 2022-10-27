from json.decoder import JSONDecodeError
import requests

payload = {"name": "User"}

response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)
print(response.status_code)


response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "Her"})
parsed_response_text = response.json()

print(parsed_response_text["answer"])

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a Json format")

# params GET request
response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1" : "huyak1"})
print(response.text)

# params POST request
response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1" : "huyak1"})
print(response.text)


# Status code
response = requests.get("https://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)

response = requests.get("https://playground.learnqa.ru/api/get_50")
print(response.status_code)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response

print(first_response.url)
print(second_response.url)


# Headers
headers = {"some_header":"123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)

print(response.text)
print(response.headers)