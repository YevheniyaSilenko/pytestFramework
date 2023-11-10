import requests
import json

def get_planet_info(planet_url):
    planet_response = requests.get(planet_url)
    planet_data = planet_response.json()
    return {
        'name': planet_data['name'],
        'climate': planet_data['climate'],
        'terrain': planet_data['terrain'],
    }

starship_url = 'https://swapi.dev/api/starships/10/'
starship_response = requests.get(starship_url)
starship_data = starship_response.json()

starship_info = {
    'name': starship_data['name'],
    'max_speed': starship_data['max_atmosphering_speed'],
    'class': starship_data['starship_class'],
}

pilots_info = []
for pilot_url in starship_data['pilots']:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()

    planet_info = get_planet_info(pilot_data['homeworld'])

    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'weight': pilot_data['mass'],
        'homeworld': {
            'name': planet_info['name'],
            'climate': planet_info['climate'],
            'terrain': planet_info['terrain'],
        },
        'homeworld_url': pilot_data['homeworld'],
    }

    pilots_info.append(pilot_info)

starship_info['pilots'] = pilots_info

with open('millennium_falcon_info.json', 'w') as json_file:
    json.dump(starship_info, json_file, indent=2)
