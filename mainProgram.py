from AdminClass import Admin, Privileges
#from Privileges import Privileges
from user import User

#UserProfile_1 = User('Rida Fatima', 'CIS', 90, 'female')
#UserProfile_2 = User('Sara Ahmed', 'BCIT', 'female', 'sara_ahmed96@gmail.com')


List_Privileges = ['can do this', 'can do that']

privilege_1 = Privileges(List_Privileges)
print(' calling privileges from class PRIVILEGES : ')
privilege_1.show_privileges(List_Privileges)

admin_1 = Admin('Rida Fatima', 'CIS', 90, 'female')
print(' calling privileges from class AdminClass : ')
# admin_1.show_privileges(ListOfprivileges)

admin_1.privileges_1.show_privileges(List_Privileges)