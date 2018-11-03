from operator import itemgetter

users = [

    {'f_name': 'Tom', 'l_name': 'Roberts'},

    {'f_name': 'Tom', 'l_name': 'William'},

    {'f_name': 'Tom', 'l_name': 'Jones'},
]

for user in sorted(users,key=itemgetter('f_name')):
    print(user)

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')

for user in sorted(users,key=itemgetter('f_name','l_name')):
    print(user)

# min and max values in a dic

prices_kurti = {
    'zeen': 4000,
    'oaks': 3200,
    'j.': 2500,
    'alkaram': 4400,
    'nishat': 2100,
}

print(min(prices_kurti.values()))                                # this gives me 2500 only but does not print J. with it

print(list(min(zip(prices_kurti.keys(), prices_kurti.values()))))  # this returns min key ( "based on the ASCII value" )

print(list(min(zip(prices_kurti.values(), prices_kurti.keys()))))  # this returns min value with IT's key