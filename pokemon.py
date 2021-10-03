from pokedex import pokedex

import random 
import requests
import json

class Generator :

    def __init__(self):
        self.pokedex = pokedex.Pokedex(version='v1', user_agent='ExampleApp (https://localhost, v2.0.1)')
        self.id_list = []

        for i in range(1,885) :
            self.id_list.append(i)
        
        with open("pokemon_list.json", "r") as file :
            file = json.load(file)
            file = self.id_list

            with open("pokemon_list.json", "w") as writing_file :
                file = json.dump(file, writing_file)

    def random_pokemon(self):
        with open("pokemon_list.json", "r") as file :
            file = json.load(file)

            id = random.choice(self.id_list)
            del file[id - 1]
            result = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/")
            result = result.json()

            for element in result['names'] :
                if element['language']['name'] == 'fr' :
                    name = element['name']

            for element in result['flavor_text_entries'] :
                if element['language']['name'] == 'fr' :
                    description = element['flavor_text']
            
            image_url = self.pokedex.get_pokemon_by_number(id)[0]['sprite']

            with open("pokemon_list.json", "w") as writing_file :
                file = json.dump(file, writing_file)


        return Pokemon(name, id, description, image_url)
        



class Pokemon :

    def __init__(self, name, id, description, image_url) :
        self.name = name 
        self.id = id 
        self.description = description
        self.image_url = image_url
