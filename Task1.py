import requests
from pprint import pprint 

def get_json(url):
    response = requests.get(url = url)
    return response.json()

def find_the_smartest(url, super_list ):
    intelligence_dict = {}
    json_list = get_json(url)
    for hero in json_list:
        if hero['name'] in super_list:
            intelligence_dict[hero['name']] = hero['powerstats']['intelligence']
    max_intell_key = max(intelligence_dict, key=intelligence_dict.get)
    return max_intell_key

super_list = ["Hulk", "Captain America", "Thanos"]
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
print(find_the_smartest(url, super_list ))
