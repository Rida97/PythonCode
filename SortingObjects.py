from operator import attrgetter

class User:
    def __init__(self, name, id):
        self.name = name
        self.userid = id

    def __repr__(self):                         # string representation of the obj ---
                                            # return a string containing a printable representation of an object.
        return self.name + " "+ str(self.userid)


# users = User('Rida', 11)   or you can make a list of users/ objects !

users = [
User('Rida', 11),
User('Sarah',20),
User('Zamp', 87),
User('Nerd', 56),
User('Burg', 21),
]

for user in users:
    print(user)

print('------------------Alphabetical Sort------------------')

for user in sorted(users, key=attrgetter('name')):
    print(user)


print('--------------------Number Sort----------------------')

for user in sorted(users, key=attrgetter('userid')):
    print(user)