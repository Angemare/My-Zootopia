
# Javascript Object notation
import json
# opens json file, with open r for read the file
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

# print list - nested structure
animals_data = load_data('animals_data.json')
print(animals_data)
print(type(animals_data))

# Task - iterate thru list + print: NAME, DIET, 1st LOCATION, TYPE
for animal in animals_data:
    print("Name:", animal['name'])
    print("Diet:", animal['characteristics']['diet'])
    print("Location:", animal['locations'][0])
    print("Type:", animal['characteristics']['type'])
    print("")




