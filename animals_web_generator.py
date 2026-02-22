
# Javascript Object Notation
import json

# opens json file, with open r for read the file
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

# print json list - nested structure
animals_data = load_data('animals_data.json')

# read content of the template html
def read_html(file_path):
    """ loads html file """
    with open(file_path, "r", encoding="UTF-8") as handle:
        return handle.read()

# Create string - reading animals data from new html "animals.html"
animals_template = read_html('animals_template.html')

# Create a function
def serialize_animal(animal_obj):
    output = ''
    #append information to each string
    output += '<li class="cards__item">\n'

    name_value = animal.get('name', 'unknown')
    if name_value != 'unknown':
        output += f"<div class='card__title'> {name_value}</div><br/>\n"

    output += '<p class="card__text">'

    characteristics = animal.get('characteristics', {})
    diet_value = characteristics.get('diet', 'unknown')
    if diet_value != 'unknown':
        output += f"<strong>Diet:</strong> {diet_value}<br/>\n"

    locations_value = animal.get('locations', 'unknown')
    if locations_value != 'unknown':
        output += f"<strong>Location:</strong> {locations_value[0]}<br/>\n"

    characteristics = animal.get('characteristics',{})
    type_value = characteristics.get('type', 'unknown')
    if type_value != 'unknown':
        output += f"<strong>Type:</strong> {type_value}<br/>\n"

    output += "</p></li>\n"

    return output

# create empty string
output = ''
# Task - iterate thru list + print: NAME, DIET, 1st LOCATION, TYPE (if given)
for animal in animals_data:
    output += serialize_animal(animal)

# replace old html with new html
new_html = animals_template.replace("__REPLACE_ANIMALS_INFO__", output )
print(new_html)

# write HTML
with open("animals.html","w", encoding="UTF-8") as handle:
    handle.write(new_html)




