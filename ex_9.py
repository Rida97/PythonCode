# from the (name of the file) import the (class) you want

from resturant import Resturant, IceCreamStand

from user import user, Admin

my_resturant = Resturant('Kababjees', 'Continental')

print(' Name of My Resturant is : ' + my_resturant.name.title())
print(' Cuisine type of my Resturant is  : ' + my_resturant.cuisineType.title())

print('\n')
your_resturant = Resturant('BBQ Tonight', 'BBQ')
print(your_resturant)

my_resturant.describe_resturant()
your_resturant.describe_resturant()

my_resturant.open_restutrant()

# EX 9.4

resturant_1 = Resturant(' Hello Ji chai peelo ', 'FastFood')

resturant_1.describe_resturant()
resturant_1.print_numberServed()                                # it should print 0
resturant_1.set_num_served(2)                                   # it should op 2
resturant_1.print_numberServed()
resturant_1.increment_number_served(3)                          # it should output 5
resturant_1.print_numberServed()

# EX 9.6
ListOfFlavors = ['Vanilla', 'Chocolate', 'Caramel', 'Blueberry']
IceCream = IceCreamStand(ListOfFlavors)
IceCream.print_flavors(ListOfFlavors)

print('\n~~~~~~~~~~~~~~~~~~~~ USER PROFILE ~~~~~~~~~~~~~~~~~~~~')

UserProfile_1 = user('Rida Fatima', 'CIS', 90, 'female')
UserProfile_2 = user('Sara Ahmed', 'BCIT', 'female', 'sara_ahmed96@gmail.com')

UserProfile_1.describe_user()
UserProfile_1.greet_user()
UserProfile_1.increment_loginAtempts()
UserProfile_1.print_loginAttempts()

UserProfile_2.describe_user()
UserProfile_2.greet_user()

UserProfile_2.increment_loginAtempts()
UserProfile_2.increment_loginAtempts()
UserProfile_2.increment_loginAtempts()

UserProfile_2.print_loginAttempts()
UserProfile_2.reset_loginAttempts()
UserProfile_2.print_loginAttempts()

UserProfile_1.print_loginAttempts()

# ex 9.7:
List_Priveleges = ['Delete a post', 'Add a new post', 'Save a user', 'Ban a user']
admin = Admin(List_Priveleges)
admin.show_priveleges(List_Priveleges)