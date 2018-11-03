# by creating a class we are creating a data type

# A Questons CLASS TELLS YOU What a Question is, what it is consist of !

class Questions:
    def __init__(self, ques, ans):   # here we are passing the attributes of the OBJECT through an initialize function
        self.ques = ques             # self is referring to the ACTUAL OBJECT !
        self.ans = ans               # here we are assigning the values of the object we passed to the object itself

# A Student CLASS TELLS YOU What a Student is !

class Student:
    def __init__(self,name,gpa,dept,rollno):              # here we define the attributes of the obj our obj should have

                                            # This basically gives the general idea of an obj you're going to make
                                            # for ex you wanted to Create an object "Student" in a program which is going to design
                                            #  his Annual report . So in this prog you wanna add the attributes of name,year,dept,cgpa,rollno .
                                            # in  a nut shell : there are so so many attributes of a studdent but we are interested in some certain
                                            # of em so we are mapping only those. and for this mapping we create classes !

        self.name = name
        self.gpa = gpa
        self.dept = dept
        self.rollno = rollno