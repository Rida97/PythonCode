# List Slicing

# Reverse a string

string = "araS adiR"

string = string[::-1]  # [start : stop : step ] [::] -> by default start at 0 go till the end , then step -1
print(string)

my_name = string[0:4]
print(my_name)

greet = 'Hello'  # 5 digits

print(greet[0:4])   # Hell   0,1,2,3 (4-1 = 3)
print(greet[0])     # H
print(greet[-1])    # o
print(greet[1:5])   # ello
print(greet[::-2])  # olH
print(greet[2:])    # llo
print(greet[::-1])  # olleH
print(greet[:])

# Write a Python statement using slice assignment that will fill in the missing values so that a
# equals [1, 2, 3, 4, 5, 6, 7, 8].
a = [1, 2, 7, 8]
a[2:2] = [3,4,5,6]
print(a)

t = ('tuple !' ,) # a trailing comma to indicate it's a tuple not an expression

a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]

