import requests


def scrape_data(url, pokemon_name):
    return requests.get(url + pokemon_name)


def get_attributes(data, pokemon_name):
    data_attr = {}
    data_attr["name"] = pokemon_name
    data_attr["id"] = data["id"]
    data_attr["height"] = data["height"]
    data_attr["weight"] = data["weight"]
    list_ability = []
    for ability in data["abilities"]:
        list_ability.append(ability['ability']['name'])
    data_attr["abilities"] = list_ability
    return data_attr
