# CREATING LISTS THROUGH RANGE FUNCTIONS -

list_num = range(2,7)

for item in list_num:
    print(item)

numbers = list(range(1, 6))             # starts from 1 go till 6 but NOT including 6 !!!
print(numbers)

even = list(range(2, 9, 2))             # go from 2 till 9 , add 2 after every iteration
print(even)

squareList = []

for value in range(1, 11):
    sq = value**2
    squareList.append(sq)           # or direct way : append(value**2)

print(squareList)

print("Starting 3 : ", squareList[0:3])
print("Middle   3 : ", squareList[3:6])
print("End ki   3 : ", squareList[-3:])

#for value in squareList:


randomList = []

for item in range(1, 7):     # [1,2,3,4,5,6]
    if item % 2 != 0:
        randomList.append(item + 1)
    else:
        randomList.append(item)

print(randomList)

Squares = [value ** 2 for value in range(2, 5)]
print(Squares)

#OneMillion = list(range(1, 1*10**6))
#print(OneMillion)
#print("\nSum: ", sum(OneMillion))
#print("Min: ", min(OneMillion))
#print("Max: ", max(OneMillion))

oddList = list(range(1, 20, 2))       # range(start,stop,step ) . by default step is 1 when only 2 parameters are given

for oddno in oddList:
    print(oddno)

# LIST COMPREHENSION :

Cubes = [value ** 3 for value in range(1, 11)]
print(Cubes)

My_Pizzas = ["Pepperoni", "Chicken Fajita"]
My_friends_Pizzas = My_Pizzas[:]
My_Pizzas.insert(0,"CreamyCheese")
print(My_friends_Pizzas)
My_friends_Pizzas.insert(0, "BBQ Pizza")

print("I love these pizzas : ", My_Pizzas)
print("My friend loves these pizzas : ", My_friends_Pizzas)

Bazgha_music = ["LP","ColdPlay"]

My_music = Bazgha_music                # IT WILL MAKE SURE THAT BOTH THE LISTs ARE ENTIRELY same throughout the prog

print("My Music: ", My_music)
print("Bazgha: ", Bazgha_music)

# Bazgha_music.append("BTS")         # this adds BTS to My_music too ! EWWWWWW BTS!

My_music.append("MAULA")             # MAULA added too Bazgha's list too but she doesnt listen to it

print("My Music: ", My_music)
print("Bazgha: ", Bazgha_music)

# TUPLES :

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = input(" Which car you want to purchase : ")

CAR = car.lower()

if CAR not in cars:
    print(" Sorry, " + car.title() + " is out of stock ")
else:
    print("For further details of " + car.title() + " visit our page . THANKYOU !")

Age = input(" Enter your age : ")

age = int(Age)

if age >= 65:
    print("Price : " + '5')
elif age < 16:
    print("Price : " + '7')
else:
    print("Price : " + '10')

# add toppings of the user according to their demand , if the list is empty print plain pizza,

userNames = ['sara', 'jon', 'elia']         # using it as current_users too

for user in userNames:
    if len(userNames) == 0:
        print("We need more users !")
    elif user in userNames:
        if user.lower() == 'admin':
            print(" hello " + user + " want to see status report ? ")
        else:
            print("hello ordinary user " + user)

new_users = ['sara', 'jon', 'poppy', 'cookie']

for User in new_users:

        if User.lower() in userNames:
            input(" Enter another username, It hasbeen used ")
        else:
            print(" Your username is fine ")




