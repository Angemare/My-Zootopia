
# Javascript Object notation
import json
# opens json file, with open r for read the file
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

# print list - nested structure
animals_data = load_data('animals_data.json')
#print(animals_data)
#print(type(animals_data))

# Task - iterate thru list + print: NAME, DIET, 1st LOCATION, TYPE (if given)
for animal in animals_data:

    name = animal.get('name', {})
    name_value = animal.get('name', 'unknown')
    if name_value != 'unknown':
        print("Name:", name_value)

    characteristics = animal.get('characteristics', {})
    diet_value = characteristics.get('diet', 'unknown')
    if diet_value != 'unknown':
        print("Diet:", diet_value)

    locations = animal.get('locations', {})
    locations_value = animal.get('locations', 'unknown')
    if locations_value != 'unknown':
        print("Location:", locations_value[0])

    characteristics = animal.get('characteristics',{})
    type_value = characteristics.get('type', 'unknown')
    if type_value != 'unknown':
        print("Type:", type_value)






    #print("Name:", animal['name'])
    #print("Diet:", animal['characteristics']['diet'])
    #print("Location:", animal['locations'][0])

    #print("Type:", animal['characteristics']['type'])
    print("")




