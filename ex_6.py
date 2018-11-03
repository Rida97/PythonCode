# DICTIONARIES :

# dic can be used to represent an alien which is of color green, occurs at level 1 etc..

alien_o = {'color': 'green', 'position': 'north-west', 'level': 1}

person = {
    'first_name': 'Smith',
    'last_name': 'Gold',
    'age': '27',
    'city': 'California',
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#Poll:

Fav_num = {
    'sara': 12,
    'John': 22,
    'Asam': 54,
    'Rida': 11,
    'Sam': 99,
    'Ali': 33,
}

print(Fav_num['Rida'])

Fav_num['Elsa'] = 23
Fav_num['Kim'] = '22'

for name, fav_num in Fav_num.items():
        print(' hey, ' + name + ' your favorite number is  :' + str(fav_num))

print('\n')

for name in Fav_num.keys():
    print(' hey, ' + name + ' Ty for taking part in the poll ! ')

print('\n')

# You can only update the value and key cannot be updated.

# ( In python you can not update a key. Only possible way is to delete the original key and create a new one.)

for name, fav_num in Fav_num.items():
    if name == 'sara':
        Fav_num['sara'] = '24'
        print(' hey, ' + name + ' your favorite number is  :' + str(fav_num))
        break
    else:
        print(Fav_num.get('name', "Not FOUND"))
        break

favourite_languages = {
    'edward': 'Python',
    'sarah': 'java',
    'Kim': 'C++',
    'eric': 'Javascript',
    'xyz': 'perl',
    'Shah': 'Ruby',
}
# Make a list of people who should take the favorite languages poll.

list_people = ['antonio', 'andy', 'edward', 'IceBerg', 'eric']

for people in list_people:
    print(people)                                   # this will return all the names in the list_people
    if people in favourite_languages.keys():    # keys mean all the names in the fav languages dictionary
        print(people + ' You have taken part in poll ')
    else:
        print(people + ' You have not taken part in poll ')

print('\n')

for name in favourite_languages:
    print(name)                      # this will return all the names in favourite_languages

print('\n Using values Function: ')

for language in favourite_languages.values():   # this prints out all the languages
    print(language)

# hobbies :

Hobbies = {
    'diego' : ['reading', 'hiking', 'teaching'],
    'lawrence': ['eating'],
    'python': ['swimmming', 'dance']
    }

for list_hobbies in Hobbies.values():
    print(list_hobbies)

for name in Hobbies.keys():
    for hobby in Hobbies[name]:
        print(name + ' loves ', hobby)


