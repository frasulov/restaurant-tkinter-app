

# pip install requests
import requests
from json import loads


url = "http://universities.hipolabs.com/search"

country = input("Please, Enter country name to see universities: ")

params = {
    "country": country
}

response = requests.get(url, params=params)

json_dict = loads(response.text)

for item in json_dict:
    print(item)


# print(response.text)