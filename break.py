# print all the multiples of 6 or the table of 6 !
# break is used when we want to exit the loop as soon as the desired condition is met and we dont want
# to loop through all the other items

for num in range(6,43):
    if num % 6 == 0:
        print(num)
        break                       # printing only 6 !


print('**************************************************************************')

for num in range(4,41):
    if num % 4 == 0:
        print(num)

# play around withthis magic no program, change the value of the range, you will figure out the use of :
# break , if , if ka else & for ka else !

magicNo = 11

for eachNo in range(10): # if range  is 11 -> 0 - 10

    if eachNo is magicNo:
        print(' magic no is: ', eachNo)
        break      # break terminate the loop as soon as the no is found due to which else of for will never be Executed
    else:
        print(' not a magic no :( ', eachNo)

else:
    print(" If I'm being printed then loop must be exhausted and the num must not be found as break statement is used\n")

list_no = [1,2,3,4,5,6,7,8,9]

for i in list_no:
    if i % 2 == 0:
        continue       # dont print even values
    else:
        print(i)
