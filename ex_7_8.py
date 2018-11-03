# For a program that should run only as long as many conditions are true,
# you can define one variable that determines whether or not the entire program
# is active.

# A loop that starts with while True u will run forever unless it reaches a
# break statement.

active = True
lives = 2
#  This prog will keep on executing the else part till I type 'quit'
#  Instead of putting all the conditions and checks inside the while loop we can create a var
#  called as flag which will be set to false y upon if any of th e condition fails then
#  While loop will only need to check flag's value

while active:
    button = input(' Quit or Continue ? ')

    if button == 'quit' or 'Quit' or 'QUIT' or 'q':
        active = False

    elif lives == 0:
        active = False

    else:
        print('Continue with the game ')


prompt = "\nEnter your age:     "
prompt += "\nEnter 'quit' when you are done! "
Active = True

while Active:
        age = input(prompt)

        if age == 'quit' or 'q':
            Active = False
        else:
            age = int(age)  # as comparison is required so convert it(str) into int
            if age < 3:
                print(' You are free to go !')

            elif age > 12:
                print(' 15$ for the ticket, please ')

            else:
                print(' 10$ for the ticket, please ')


responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response                                                         #dictionary [ key ]

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(name + " would like to climb " + response + ".")























