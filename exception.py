# print(result)  it will return this : ZeroDivisionError: division by zero , ZeroDivisionError is an object

num = input(' Enter any number : ')

try:
    result = 5/int(num)                # I csn enter 2,3 or 0 ! On entering any no EXCEPT zero then this try block will
    print(result)                      # execute its code. it will look for except block only if an error occur in try
except ZeroDivisionError:                           # block. it will then look for relevant exception in except block
    print('Cannot divide by 0 !')
except ValueError:
    print('Enter no only !')

#######################################################################################################################

print("Give me two numbers, and I'll divide them.")
print("Enter 'quit' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'quit':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print(' Enter number only ')
  #  else:
   #     print(answer)

# 1) The only code that goes in the try block is the one thst might raise an error or exception
# 2) What should you write in else block ?
# ans)  the code that you want your proggram to run only if no exception is raised or the try block was successful
print('\n')

# len : this func returns no of characters if its called with a string -> len(String) -> 6
# len : returns the no of elements in an array/list -> ['abc', 'xyz'] -> 2

filenames = ['ALICE.txt' , 'Angels And Demons.txt']
try:
    for filename in filenames:
        with open(filename) as f_obj:
            contents = f_obj.read()
except:
    FileNotFoundError:\
        print(' The file ', filename, ' doesnot exist !')
else:
    spliited = contents.split()
    print(contents)
    print(spliited)                                                  # it splits the words
    print('alice.txt file has ' + str(len(spliited)) + ' words')  # now you csn count the WORDS
    print('length: ', str(len(contents)))                    # this returns 25, as it counts all the leeters with spaces














