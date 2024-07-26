import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2' 
TOKEN = '504534bd4560d697c23fafa6bf3387a1'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '4516'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID}) 
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['id'] == '4516'

