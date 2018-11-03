class Student():
    def __init__(self, name, **student_info):
        self.name = name
        # we need to unpack this invisible dict into our own handmade dict !
        Info = {}
        Info['name'] = name

        for eachKey, eachValue in student_info.items():
            Info[eachKey] = eachValue
        for eachKey, eachValue in Info.items():
            print(Info)
            break



class student():
    def __init__(self, firstname = 'Syed', Class= '5'):    # we have to initialize the attributes otherwise an error
        self.name = firstname                              # will occur
        self.Class = Class

    def get_student(self):
        print('Name Student: ' , self.name + '\nCLass is:', self.Class)


