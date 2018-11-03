from collections import Counter,OrderedDict

def QuestionsMarks(s):
    a, b = 0, 0
    for i in range(len(s)-1):
        for j in range(i, len(s)):
            if s[i].isdigit() and s[j].isdigit() and int(s[i]) + int(s[j]) == 10:
               a, b = i, j
    new = s[a+1:b+1]
    if new.count('?') == 3:
        return 'true'
    else:
        return 'false'
print(QuestionsMarks("acc?7??sss?3rr1??????5"))

def QuestionsMarks(s):
  qnum = 0
  dig = 0
  has_10 = False
  for ch in s:
    if ch.isdigit():
      if int(ch) + dig == 10:
        if qnum != 3:
          return 'false'
        has_10 = True
      dig = int(ch)
      qnum = 0
    elif ch == '?':
      qnum += 1
  return 'true' if has_10 else 'false'

string = "fun&!! time"

l = string.split()
print(l)

def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    print('sum = ',sum)
    return sum


# using max(arg1, arg2, *args, key)
print('Maximum is:', max(100, 321, 267, 59, 40, key=sumDigit)) # sum = 1,6,15,14,4 . the largest sum is third value in the list -> 267

# using max(iterable, key)
num = [15, 300, 2700, 821, 52, 10, 6]
print('Maximum is:', max(num, key=sumDigit))

# find list with max length using key = len

def LongestWord(sen):
    # first we remove non alphanumeric characters from the string
    # using the translate function which deletes the specified characters
    sen = sen.translate("~!@#$%^&*()-_+={}[]:;'<>?/,.|`")

    # now we separate the string into a list of words
    arr = sen.split(" ")

    # the list max function will return the element in arr
    # with the longest length because we specify key=len
    return max(arr, key=len)


print(LongestWord("the $$$longest# word is coderbyte"))

arr = [3, 5, 2, -4, 8, 11]
sum = 7

for i in range(0, len(arr)):
    for j in range(1, len(arr)):

        if arr[i] + arr[j] == 7:
            print(arr[i], ' + ' , arr[j] , '= 7')
        else:
            continue

word = 'GOOGLE'
counter = Counter(word)
commomword = counter.most_common(len(word))
print(commomword)


value = input(' enter values : ')     # enter values separated by comma. value contains = '1,2,3'
print(value)
list = value.split(",")               # split will treat every word b/f , a separste term so returning '1'
# print(int(list_value)
print(list)                        # as input is in string form and we are displaying all the values in one go
                                    # so we cannot use int as it accepts a single string only

valuesList = []
for i in range(1,4):
    values = input(' enter values : ')
    valuesList.append(int(values))  # here we r taking each value at the time of taking the input & converting it to int

print(valuesList)




