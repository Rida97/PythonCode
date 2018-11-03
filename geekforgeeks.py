# how to handle missing keys in a dictionary ?
# way 01 : Use the get method to retrieve user inputs and put default in it
# way 02: Use try except method


import collections
dict_name = {
    'name1' : 'rida',
    'name2' : 'Sara',
}
try:
    print(dict_name['name1'])   # it prints rida

    print(dict_name['name2'])    # it prints Sara

    print(dict_name['name3'])  # KeyError: 'name3'

# keyError: user trying to access the key that is not present in the dict
except KeyError:
    print(' Not Found ')
    #print(dict_name.get('name2', 'not found'))
    #print(dict_name.get('name3', 'not found'))

# way 02:
userInput = input(' enter name : ')              # user will enter a value here !


if userInput not in dict_name.values():        # use set default when you want ot give the mpression to the user that the value they entered was present in the key
                                               # even if it wasnt
    dict_name.setdefault('name4', userInput)
    for val in dict_name.values():
     print(val)
else:
    print(userInput)

# way 03:
# it is a better approach than get b/c you dont need to call a function again and again, and so you dont need to pass
# the default value again and again. faster, time saving, no need of KeyError Exception handling as well !!!!

dict_name = collections.defaultdict(lambda :'Key Not Found ')

print(dict_name['name3'])
print(dict_name['name4'])

dict_flowers = {
    'flower1' : 'daisy',
    'flower2' : 'roses',
    'floswer3' : 'jasmeen',
}
dict_fruits = {
    'fruit1': 'orange',
    'fruit2': 'pineapple',
    'fruit3':'tomatoe',
}

chain = collections.ChainMap(dict_flowers,dict_fruits)              #if both the dic have same key(s) then the key(s)
print('\n Printing Chain Map:')                                            # will appear only once i.e key  of the first dict only
print(chain.maps)
print('\n Keys of Chain:    ')
print(list(chain.keys()))
print('\n Values of Chain:  ')
print(list(chain.values()))

dict_veg = {
    'veggie1': 'potaatoe',
    'fruit3': 'tomatoe',
    'veggie3': 'onion',
}

block = chain.new_child(dict_veg)
print('\n Printing Block map:')
print(block.maps)
print('\n Keys of Block:    ')          # key : fruit3 appear once
print(list(block.keys()))
print('\n Keys of block:    ')
print(list(block.keys()))
print('\n Values of Block:  ')         # value : fruit3 appear once
print(list(block.values()))

