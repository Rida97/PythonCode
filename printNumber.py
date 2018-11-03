import json
filename = 'numberSaved.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    for number in numbers:
        print(number)