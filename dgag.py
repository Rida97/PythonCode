prompt = "\nEnter your age:     "
Active = True
Exit = ' Press e for exit '
while Active:
    age = input(prompt)

    age = int(age)
    if age < 3:
        print(' You are free to go !')
    elif age > 12:
        print(' 15$ for the ticket, please ')
    else:
        print(' 10$ for the ticket, please ')

    Exit = input('\t\nDo you want to continue(yes/no :)   ')
    if Exit == 'no':
        Active = False
print(' Deli Sandwiches had run out of Pastrami ! ')
ordered_sandwiches = ['pastrami', 'tuna', 'club', 'pastrami', 'sausage', 'club', 'pastrami']
finished_sandwiches = []

while 'pastrami' in ordered_sandwiches:
    ordered_sandwiches.remove('pastrami')

while ordered_sandwiches:
    sandwich = ordered_sandwiches.pop()
    print(' I made your', sandwich + ' sandwich ')
    finished_sandwiches.append(sandwich)
print('\n')

for sandwich in finished_sandwiches:
    print(sandwich, ' sandwich was made ')





