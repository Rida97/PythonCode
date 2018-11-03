from StudentClass import student

class Person():
    def __init__(self,name,age,city,gender='Female'):
        self.Name = name
        self.Age = age
        self.City = city
        self.Gender = gender

    def getPerson(self):
        print('Name:    ', self.Name + '\nAge:     ', self.Age + '\nCity:    ', self.City + '\nGender:  ', self.Gender)


class Teacher(Person):
    # pass

    def __init__(self, name, age, city, gender, subject, salary):      # this init function is of Teacher !
        super().__init__(name, age, city, gender)          # super func will call the init func of Person (Parent class)
        self.Subject = subject                           # adding an attribute that is specific to Teacher (child) only!
        self.Salary = salary

        # INSTANCES AS AN ATTRIBUTE !! --> student() will make an instance of a student and save it as an att of Teacher
        self.Student = student()

    def print_teacher(self):
        print('Subject: ', self.Subject + '\nGender : ', self.gender)

    def getTeacher(self):
        self.getPerson()                                             # calling thr func of parent class
        print('Subject: ', self.Subject + '\nSalary:  ', self.Salary)




