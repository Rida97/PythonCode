from math import *

names = ["ada", "Ada", "ADA", "adA", "aDA","ADa","AdA"
           ]

for name in names:
    print(name.title())    # .title will make all the possibilites of the input to a standard naming convention i.e : Rida , John
                           # now a/f using this method you dont have to worry about the format in which USER enters his name

stringg = "python ".rstrip()
print(stringg)

first_name = input("Please, enter your first name : ")

print(first_name)

print(" Right ,left, Strip functions: ")

print(first_name.rstrip())
print(first_name.lstrip())
print(first_name.strip())

quote1 = "Albert Einstein once said," + '"A person who never made a mistake never tried anything new."'

print("Albert Einstein once said," + '"A person who never made a mistake never tried anything new."')

print(quote1)

print(9-1)
print(16/2)
print(7+1)
print(4*2)

Things_to_buy = ["shoes","clothes","bags","books"]   # list of things that dont relate with eachother
print(Things_to_buy)

for thing in Things_to_buy:
    print(thing.title())

# want to access the last item in the list but dont know how LONG the list is  ?
# Dont worry ! there's an easy sol for that ! use -1

print(Things_to_buy[-1])   # will gv you the last thing !

add_new_item = "specs"

Things_to_buy.append(add_new_item)

print(Things_to_buy)

grocery_list = ["vegetables", "crockery", "fruits"]

print(Things_to_buy.extend(grocery_list))                      # error : Things_to_buy.insert(0, "grocery_list")

Things_to_buy.extend(grocery_list)
print(Things_to_buy)

# remove func :  remove an item by its name, you can use the removed item just like in pop

print(Things_to_buy.remove("fruits"))  # error : print(remove("fruits","specs")) accepts only 1 item at a time
print(Things_to_buy)

Things_to_buy.remove("specs")
print(Things_to_buy)

# POP and DELETE DIFF
# numbers removed through pop can be used later in the prog.but del DELETES them permenantly !


numbers = [0, 1, 2, 3, 4, 5]

for num in numbers:
    print(num)


print(numbers.pop(0))
print(numbers)

popped_number = numbers.pop()                     # .pop() : empty () will REMOVE the LAST element by DEFAULT
print(popped_number)

print(numbers)                                     # it will print [1,2,3,4]


#    error :      deleted_number = del numbers[3]  #   you cant assigned the deleted value b/c it doesnt exist anymore
# print(deleted_number)
del numbers[3]                                     # it will delete 4 from the list

 # ex : 03

guest = ["nani", "javeria", "fariya"]

invitation = "Have dinner at my house on Sunday  "
print(invitation + guest[0])
print(invitation + guest[1])
print(invitation + guest[2])

print(guest[0] + " cant make it to the dinner")

guest[0] = "Ayesha"

print(invitation + guest[0])
print(invitation + guest[1])
print(invitation + guest[2])

print(" Oh wait !I found a biiger table, lets invite more people ")  # at the start,mid,end

guest.insert(0, "Mahnoor")
print(len(guest))
mid_length = (len(guest))/2
print(mid_length)

print(ceil(mid_length))

guest.insert(int(mid_length), "Laaebba")

guest.append("Asm")

for index_value in range(len(guest)):
    print(invitation + guest[index_value])

print("you can invite only two people for dinner.")

un_invite = " "
while len(guest) != 2:

    un_invite = guest.pop()
    print("sorry " + un_invite + " I cant invite you to the dinner. ")

for i in range(len(guest)):
    print(" you are still invited " + guest[i])

print(len(guest))

print('List before del: ', guest)

del guest[:]

print(" list is empty ")
print(guest)

lst_del = [7, 14, 21, 28, 35, 42]

print('List before del: ', lst_del)

del lst_del[2:5]                           # [7,14,42] starting from 2 till 5-1 ,delete all //  delete from starting pt till end pt -1
print('List After del: ', lst_del)


cars = ["prius", "BAleno", "mirA", "Alto"]

print("Before sorting                 : ", cars)

print("After sorting thru Sorted func : ", sorted(cars))

print("Orignal list                   : ", cars)

cars.sort()
print("After sorting thru Sort func   : ", cars)

print("Orignal list                   : ", cars)

for i in range(len(cars)):
    print(cars[i].lower())

















