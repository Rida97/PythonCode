from modules import print_name
# classes , difference between CLASS Variables and INSTANCE variables :

class Student:

    Class_of_Student = 5          # Class var, common att shared by all the objects

    def __init__(self, name, gender): # name, gender are unique attributes of all students
        self.name = name
        self.gender = gender

      #  print_name(name)     you can also use this function

        print(name, gender) #, Class_of_Student )  b/c now you're inside init function scope

    def print_all(self):
        print(self.Class_of_Student, self.name, self.gender)


student1 = Student('Ali', 'Male')
print(student1.Class_of_Student)
student2 = Student('Elsa', 'Female')
print(student2.Class_of_Student)

student1.print_all()