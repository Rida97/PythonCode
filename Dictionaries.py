import json
# To execlude repition in ditionaries use set(), to sort the list alphabetically use sorted():
# set(stones.keys()) ,  sorted(stones.values)

stones = {
    'Ruby' : 'red',
    'Emerald': 'green',
    'Topaz' : 'yellow',
}

print('Stones: ')

for eachKey, eachValue in stones.items():
   print(eachKey + ', Color:', eachValue)

List_of_fav_colors = ['yellow', 'red']

for color in List_of_fav_colors:
    if color in stones.values():
        print('\nYour favourite color ' + color + ' is in the Dictionary of Stones too !')

print(stones['Ruby'])

users = {
   'Sara' : { 'full_name': 'Sara Ahmed',
              'University' : 'NED',
              'age': '22',
             },

    'Ali' : { 'full_name' : 'Ali Khan',
              'University' : 'JSMU',
              'age': '23',
            },
         }

for username, user_info in users.items():     # user_info is fullname,ae etc
    print("\nUsername: " + username)
    full_name = user_info['full_name']
    uni = user_info['University']
    age = user_info['age']
    print(full_name, " ", uni , " ", age , " ")

user_name = input(' enter Username: ')
password = input( ' Enter password: ')
users_dummy = {
    user_name :  { 'password' : password
                 },


}


filename = 'dictionaryTesting.json'
with open(filename,'w') as fp:
    json.dump(users,fp)
    json.dump(users_dummy,fp)














