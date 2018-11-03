from __future__ import print_function

# id() function is used to return the identity of an object.
# Python3 program to show that
# both string hold same identity
# string1 and string2 both point to same object or same location
'''
string1 = "Hello"
string2 = "Hello"

print(id(string1))
print(id(string2))

string1 += 'World'
print(id(string1))

string3 = 'rida'
print(id(string3))
'''
for row in range(1, 4, 1):   # start from 1, end at 4 -1 = 3, step size = 1 (by default = 1 )
    for col in range(row): # just think of the no where i wanna stop then add 1 to it.
         print('*', end=' ')
    print()

for row in range(3, 0, -1):  # start from 3, end at 2 -1 = 1, step size = -1
    for col in range(row):   # just think of the no where i wanna stop then subtract 1 to it.
         print('#', end=' ')
    print()

print('\n')

for i in range(3):  # 0,1,2
    print(i)

# UnPacking Arguments

def packing_function_1(*myList):

    for val in myList:
        print(val)
    print(myList) # tuple


my_list= [1,2,3,4]
# unpacking_function(my_list) TypeError: unpacking_function() missing 3 required positional arguments: 'b', 'c', and 'd'

packing_function_1(my_list)  # prints [1,2,3,4]


def unpacking_function_2(a,b,c,d):
     print(a,b,c,d)


my_list2 = [11,81,32,44]

unpacking_function_2(*my_list2)     # unpacking_function(my_list) TypeError: unpacking_function() missing 3 required
                                            #  positional arguments: 'b', 'c', and 'd'

a = input('a:   ')
b =input('b:    ')
c=input('c:     ')

if int(a) > int(c) and int(b) > int(c):
    print('smallest is c ', c)
elif int(c) > int(a) and int(b) > int(a):     # else:
    print('smallest is a ',a)                   # if ():
else:                                           # else:
    print('smallest is b ', b)

# [on_true] if [expression] else [on_false] -----> ternary operator .

def small(a,b,c):
    return c if a > c and b > c else (a if c > a and b > a else b)

print(small(2,5,7))
print(small(3,-4,2))
print(small(0,3,-1))

# import pdb
# pdb.set_trace()