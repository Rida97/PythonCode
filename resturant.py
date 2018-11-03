class Resturant():
    def __init__(self,name, cuisineType):               # note that number_served is not passed in the parameters b/c it is set by default
        self.name = name
        self.cuisineType = cuisineType
        self.number_served = 0                          # Default Value

    def open_restutrant(self):
        print(' The resturant is open now ')

    def describe_resturant(self):
        print(' Name of the resturant is : ' + self.name)
        print(' Cuisine Type is          :' + self.cuisineType)

    def print_numberServed(self):
        print(' You served : ' + str(self.number_served) + ' Customers today !\n')

    def set_num_served(self, number):
        self.number_served = number                                  # self is an attribute ( an OBJECT Attribute !)

    def increment_number_served(self, num):
        self.number_served += num


# number_served = 0 "default value"
# set_num_served(number_served = 3/4/5)
# increment_number_served()  # lets you increment the number_served by the res

class IceCreamStand(Resturant):
    def __init__(self, ListOfFlavors):
        self.ListOfFlavors = ListOfFlavors

    def print_flavors(self, ListOfFlavors):
        for self.flavor in ListOfFlavors:
            print(self.flavor)










