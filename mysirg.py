# program to print N prime numbers.
# 2,3,5,7,11,...12/(2) = 6
def prime_no(Num):
    list_num = []
    n = 3
    for i in range(2,Num):   # 2,3,4,5

        if n % (i - 1) == 0:
            print('non prime no: ', i)
            n += 1

        else:
         print('prime no :', i)
         list_num.append(i)
        if len(list_num) >= int(Num):
            break
    return list_num

Num = input(' entr the no of prime numbers you want to check :')
num = int(Num)
listno = []
listno = prime_no(num)
print(listno)


def next_primeno(num):
    n = num+1
    for i in range(2,100):
        if n//i == i or n%2 == 0 or n%i :
            n = n + 1
            print('num not prime', n)
    else:
        return n

print('ans: ')

print(next_primeno(24))




