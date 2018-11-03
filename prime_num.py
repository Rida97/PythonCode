for i in range(2,7):
    if i % 2 ==0:
        print(i)


def is_the_no_prime(num):   # 25

    for i in range(2,num):  # 2--24
       # print('i: ', i)
        print(str(num) + '% ' + str(i),' = ', num % i)
        if num % i == 0:
            print(num, ' -> non prime')
            break
    else:                            # you can saythis is for ka else, when all the possible conditions
        print('prime no')              # are exhausted we say that the num is prime

print('\n')

is_the_no_prime(25)

# Python program to check if the input number is prime or not


num = 21

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):     # if num is 5 then this loop goes from 2-4
        if (num % i) == 0:      #
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)  # 21 // 3 = 7
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")
