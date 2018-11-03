# There are2 ways to print the data that is passed in the ARGUMENTS :
# 1st way is to just saved the data inside a dictonary and then return
# the dictionary, which willbe printed out just as done on page 152 (book)
# 2nd way is to saved the data inside a dic then loop through that dic instead
# of RETURNING that dic ! so it will be printed in a much clearer and nicer way!


def user_profile(first, **user):
    UserProfile = {}
    UserProfile['firstName'] = first
  #  UserProfile['lastName'] = last
    for key, value in user.items():
        UserProfile[key] = value
    for User in UserProfile.values():
        print(User)


   # return UserProfile


print('\n User 01: ')
user_profile('Rida Fatima', city='Karachi', education='UGRAD', gender='female')
print('\n User 02: ')
user_profile('ghh fsffsa', city='Islamabad', education='GRAD', gender='male')

#USER_PROFILE = user_profile('Rgadjkga', 'fhtyue', city='Lahore', education='GRAD', gender='female')
# print(USER_PRRFILE)

