
from user import User
from Privileges import Privileges

## Here we use AN INSTANCE AS AN ATTRIBUE IN A DIFFERENT CLASS W/O INHERITANCE !


class Admin(User):

    def __init__(self, name, *User):    # it will make an object of user class !

        super().__init__(name, *User)      # This line tells Python to
                                           # call the __init__() method from Admin’s parent class(User),
        #                                   which gives an
                                           # Admin instance all the attributes of its parent class(User).

        self.privileges_1 = Privileges(List_Privileges=0)  # Make an instance / obj of the previlege and store it to privileges_1
                                          # any Admin instance will now have a Privilege instance created automatically.


class Privileges():
    def __init__(self, List_Privileges):
        self.List_Privileges = List_Privileges

    def show_privileges(self , List_Privileges):
        for self.privilege in List_Privileges:
            print(self.privilege)


