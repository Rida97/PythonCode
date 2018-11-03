import json

numbers_list = [1,2,3,4,5,6,7]             # list : Temporary data structure

filename = 'numberSaved.json'             # EMPTY file created to save the data structure contents
                                      # using with will ensure to close the file when its not being used so we dont have
with open(filename, 'w') as f_obj:  # to worry about that. 'w' open file to perform writitng.
    json.dump(numbers_list, f_obj)   # Now json is allowed to wwrite into the file

## A code to VERIFY UserACCOUNT , i.e password and username;
# first sign up then make a sign in

option = input(' Sign Up / Sign in ? ')
if option == 'signup':
    print(' ~~~~~~~~~~~~~~~~~~~~Sign Up ~~~~~~~~~~~~~~~~~')
    count = 0

    username = input('Enter your username :')
    password = input('Enter your password:')
    user_info_2 = {}
    user_info_2['username'] = username
    user_info_2['password'] = password

    Filename = 'user_account.json'
    with open(Filename,'w') as F_obj:
        json.dump(user_info_2,F_obj)

        count += 1

elif option == 'signin':

    print('\n ~~~~~~~~~~~~~~~~~~~Sign In ~~~~~~~~~~~~~~~~~~\n')
    Filename = 'user_account.json'
    Username = input(' Username: ')
    Password = input(' Password: ')

    with open(Filename) as F_obj:
        user_Info = json.load(F_obj)
        print(user_Info.values())
        print(user_Info.keys())
        name = user_Info['username']
        passWord = user_Info['password']
        print('name saved as:, ', name)
        print('password saved as: ', passWord)              # this will return the password saved in the json file !

        if name == Username:
            if passWord == Password:
                print(' Account Verified. ')
            else:
                print(' Password does not match. ')
        else:
            print(' Username doesnot match')

            # if i give key to python it will return me the vslue as an output
else:
    print(' Incorrect entry\n ')


