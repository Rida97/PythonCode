# this example is to show that how we can create a Child class that is exactly same as its parent class.
# if a child does not have any of the SPECIFICATIONS of its own then we csn use "pass" inside the child class
# that will create child class object with all the attributes/methods of parent class


from PersonClass import Teacher
from StudentClass import student

teacher_1 = Teacher('Rida', '21', 'Karachi', 'Male','Maths','25000')        # I can access person's attributes and its
teacher_1.getPerson()                                       # methods w/o creating a person Object. Python
                                                           # will create person object automatically when
print('\n')                                                           # a child obj is called

teacher_2 = Teacher('Sara', '26', 'Karachi', 'Female', 'English', '23000')
teacher_2.getTeacher()

teacher_1.Student.get_student()                    # just like using teacher_1.subject