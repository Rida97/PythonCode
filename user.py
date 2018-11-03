# EX 9.3 & 9.5

class user():
    def __init__(self, name, *user):
        self.name = name
        self.user = user
        self.login_attempts = 0

    def print_loginAttempts(self):
        print(str(self.login_attempts) , ' Login Attempts were made')

    def increment_loginAtempts(self):
        self.login_attempts += 1

    def reset_loginAttempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print('UserName : \n' + self.name + '\nOther info : ')
        for User in self.user:
            print(User)

    def greet_user(self):
        print('\nHello ' + self.name)

class Admin(user):
    def __init__(self, List_Privileges):
        self.List_Priveleges = List_Privileges

    def show_priveleges(self , List_Privileges):
        for self.privelege in List_Privileges:
            print(self.privelege)

