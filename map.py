# from operator import add
# map function
# we used list and perform and task on each item of the list. and for that we used loops
# for ex i have students with their total exmaination marks nd i want to calculate their percentages:

# WAY 01 : using loop to get each item, more lines of code, xtra things: list,append,return that list and loop ofcourse

student_marks = [455,486,538,334,545,312,447]
percent_list = []

def percentage():
    for eachstudent in student_marks:
        percnetage= (eachstudent/580) * 100
        percent_list.append(percnetage)
    return percent_list


p_list = percentage()
print(p_list)

def calculate_percent(Stud_marks):
    return (Stud_marks/580) * 100


Percentages_list = list(map(calculate_percent, student_marks))
print(Percentages_list)


def double_money(my_income):
    return my_income * 2     # we write here what we want to do with every item of the list.


income = [10, 20, 45]

new_income1 = double_money(income)
new_income2 = list(map(double_money, income))  # this line means map func says : call the func 'doublemoney' and also
print(new_income1)                       # passed the list to the func and do whatever is in the func to each and every
print(new_income2)                       # item of the list

x = [1,2]
y = [4,5,6,9]

def add_xy(x,y):
    return  x + y


op = list(map(add_xy, x, y))  # output [5, 7]
print(op)

new_tuple = map(None, x, y)
print(new_tuple)
