# lambda
# they are one time use small functions
# they are used in tkinter. for ex with buttons to give special functionality to it. every button would a specific task
# to be done (not over and over again) so for 1 time use you must use lambda & for over and over again use,use functions

# in ans we return the value = lambda is an unnamed function x is an arg : here goes all the body part of the function:
answer = lambda x: x+100

print(answer(5))

full_name = lambda first_name,second_name: first_name + " " + second_name

print(full_name('Sara','saif'))

F_name = ['Rida', 'Laaebba', 'Mahnoor']
L_name = ['Fatima', 'Memon', 'Biharan']

from itertools import zip_longest
for i, j in zip_longest(F_name, L_name):
    print(i, j)

print('------------------------------------------------------------------')

def full_name(F_name,L_name):
    return F_name + " " + L_name

full_names = list(map(full_name,F_name,L_name))

print(full_names)

for name in full_names:
    print(name)

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print(filter(lambda a, b : a == b in a, b))  # prints out [2, 3, 5, 7]

