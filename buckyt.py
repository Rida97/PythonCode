# UNpacking of a list !

# school = ['Rida Fatima',12,'C']
name, Class,section = ['Rida Fatima', 12, 'C'] #  while assign variables to EACH item of the list else an error will occur
print(name, Class , section)

def drop_first_last(grades):
    first,*middle,last = grades
    avg = sum(middle)/len(middle)
    print('Average : ', avg)

drop_first_last([55,77,87,44,34,72])

# ZIP: zipping a list to a list of TUPLES !

names = ['cs-090',  'cs-083', 'cs-142']
OOP_marks = [65, 81, 79]

# in order to display the rollnos with their corresponding marks I need to loop their both of em and use print statement
# or an easy and short way to do this to ZIP em together .

name_marks = zip(names, OOP_marks)  # [('cs-090',6),('cs-83',8),('cs-142',7)]

print('\nList Of Rollno & OOP MARKS : ')
print(list(name_marks))                     # list of tuples ^

#for k,v in name_marks:
 #   print(k,v)

# an ex of zip to calculate best of two marks of a quiz of a student

quiz_1 = [4, 9, 3]
quiz_2 = [6, 0, 5]

print(' Highest marks in quiz 1 : ', max(quiz_1))
both_quiz = zip(quiz_1, quiz_2)

finalmarks = []

def marksEvaluation():
    for marks1, marks2 in both_quiz:
        if marks1 > marks2:
            finalmarks.append(marks1)
        else:
            finalmarks.append(marks2)

    return finalmarks


print('\n Rollno & Quiz best of 2 MARKS :')

marks = marksEvaluation()

student_marks = zip(names,marks)
for student,max_marks in student_marks:
    print(student, max_marks)


books = {
    'Angels And Demons': 4.9,
    'Alice in the wonderland' : 4.4,
    'Mindwalker': 3
}

print(' The book with Min Rating is : ')
print(min(zip(books.values())))                    # returns (3,)
print(min(books.values()))                        # returns 3
print(max(books.values()))

print('     The book with Max Rating is : values, names')
print(max(zip(books.values(), books.keys())))   # here zip function is required
print('      The book with Max Rating is : names,values ')
print(max(zip(books.keys(),books.values())))

print('     Sorted books : by value / ratinr\n')
print(sorted(zip(books.values())))
print('      Sorted books : by keys / Names')
print(sorted(zip(books.keys())))
























