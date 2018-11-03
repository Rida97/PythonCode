x, y = 10, 20                                         # 1 In-Place Swapping Of Two Numbers.
x, y = y, x
print(x, y)

a ="GeeksForGeeks"                                   # 02
print("Reverse is", a[::-1])

a = ["Geeks", "For", "Geeks"]                         # 03
print(" ".join(a))

import os;                                         # 04 print path of the imported modules
import socket;

print(os)
print(socket)

def x():
    return 1, 2, 3, 4                            # 05 : return multiple values


a, b, c, d = x()
print(a, b, c, d)

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]      # 06 Find The Most Frequent Value In A List.
print(max(set(test), key = test.count))


from collections import Counter


def is_anagram(str1, str2):                 # 10  Checking if two words are anagrams
    return Counter(str1) == Counter(str2)


print(is_anagram('geek', 'eegk'))
print(is_anagram('geek', 'peek'))

a = [1, 2, 3]
x, y, z = a                              # 11 store all list items in separate var


def any_value():                        # 12 returning morethan value
    return 11, 7, 1997


A, B, C = any_value()
print(A, B, C)


def test(k1, k2, k3):                # 13 Unpack arg using SPLAT * operator
    print(k1, k2, k3)

testDict = {'k1': 1, 'k2': 2, 'k3': 3}
testList = [10, 20, 30]

test(*testDict)
test(**testDict)
test(*testList)

t1 = (1, 2, 3)                        # 14 create a dict from 2 related tuples
t2 = (10, 20, 30)
print(' create a dict from 2 related tuples ')
print(dict(zip(t1, t2)))

import itertools
test = [[-1, -2], [30, 40], [25, 35]]
print(list(itertools.chain.from_iterable(test)))

def xswitch(x):
    return xswitch._system_dict.get(x, None)

xswitch._system_dict = {'files': 10, 'folders': 5, 'devices': 2}

print(xswitch('default'))
print(xswitch('devices'))

                                           #  15 Convert a list to a dictionary

lists = ['Smith','John','Drake', 1012,3444,1857]
print(dict(zip(lists[:3], lists[3:])))

names = ['Sarah', 'Flora', 'Selena']
ids = [111,113,456]
print(dict(zip(names, ids)))

                                         # 16  Use sorted(list) to keep the original list
a = [3, 2, 1]

a2 = sorted(a)
print(a, a2)

a3 = a.sort()
print(a, a3)