
iphone = True
if iphone:                           # this condition will only execute if the cond is true
    print(" Expensive ")

iphone_8_is_expensive = False
if iphone_8_is_expensive != True:
    print(" expensive")

motorolla = True
if motorolla:
    print("Cheap")

for index in range(3,10):
    print(index)

friends = ["sara","jon","sam"]
length_of_list = len(friends)
print("List length : " + str(length_of_list))

for i in range(len(friends)):
    print(friends[i])
                                        # OR
for index_value in friends:
    print(index_value)         # By index value I mean the Contents of the list i.e "sara"

# make a function that can calc users  given power of the desired num




# LIST INSIDE A LIST OR 2D LIST !

two_dList = [
    ["a","b"],              # 0th row
    ["c","d"],              # 1st row
    ["e","f"],              # 2nd row
    ["g","h"],              # 3
    ["i","j"],              # 4
    ["k","l"],              # 5
    ["m"]                   # 6
# col 0 , 1
]

print(two_dList[0][0])                    # a
print(two_dList[4][0])                    # i
print(two_dList[5][0])                    # k
print(two_dList[1][0])                    # c
print(two_dList[3][0])                    # g
print(two_dList[1][1])                    # d
print(two_dList[4][1])                    # j
print(two_dList[5][1])                    # l
print(two_dList[3][1])                    # h
print(two_dList[0][1])                    # b
print(two_dList[2][0])                    # e
print(two_dList[0])                     # m
print(two_dList[2][1])                    # f


print(two_dList[0])                       # returns : ['a','b']
for row in two_dList:
    for col in row:
        print(col)

