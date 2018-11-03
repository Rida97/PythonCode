from questionClass import Questions

from questionClass import Student



Question = [
    "Who is the author of ANGELS AND DEMONS ? \na) Mike Dane\nb) David CopperField\n c) Dan Brown\n\n",
    "What is the National Flower of Pakistan ? \na) rose \nb) jasmeen \nc) cauliflower\n\n",
    "How many PSLs have been conducted ? \na) 4 \nb) 3 \nc) 2\n\n",
]

# make object of the class Questions:

# question = Questions(Question) # wrong way !

questions = [
    Questions(Question[0],"c"),
    Questions(Question[1],"b"),
    Questions(Question[2],"b"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
        ans = input(question.ques)
        if ans == question.ans:
            score += 1
    print(" Your score is : " + str(score) + " out of  " + "3")


run_quiz(questions)

 # Creating an ACTUAL STUDENT that has some SPECIFIC name, gpa, dept, rollno is called CREATING AN OBJECT !!!!

student1 = Student("Rida",3.2,"CS",90)
print(student1.name)