class Privileges():
    def __init__(self, List_Privileges):
        self.List_Privileges = List_Privileges

    def show_privileges(self , List_Privileges):
        for self.privilege in List_Privileges:
            print(self.privilege)


