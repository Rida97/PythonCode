gender = ""
def get_gender(gender = 'unknown'):
    if gender is 'm':
        gender= 'male'
    elif gender is 'f':
        gender = 'female'
    print(gender)


get_gender('m')
get_gender('f')
get_gender()

def work(noun = 'sara', verb='jumps on', item = 'bed'):
    print(noun, " " , verb,  " ", item)


work('Rida', 'eats', 'apple')
work('he', 'loves', 'cats')
work('watch', 'anime')              # watch anime bed  !
work(verb ='watch', item ='anime', noun='ali')  # ali watch anime , order of arg can change, but use = with it then

# flexible no of arguments:

def print_name(*names):
 #   for Every_name in names:   this is wrong as this loop while run 2 times (if there are 2 names) for 1 whole tuple
        print(names)

def sum(*numbers):
    sum = 0
    for Every_no in numbers:
        sum += Every_no
    print(sum)

print_name('rida', 'fatima')

sum(1,2,3,4,5,6,7,8)
sum(1,1,1,1,1,1,1,1)
sum(0)
sum(4,5)
