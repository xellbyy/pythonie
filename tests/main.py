import requests


URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = '504534bd4560d697c23fafa6bf3387a1'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "45085",
    "name": "jae",
    "photo_id": 2}

body_catch = {
    "pokemon_id": "45085"
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text)


response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change )
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch )
print(response_catch.text)
