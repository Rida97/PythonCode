from collections import Counter    # this Counter is a Class

nos = [1,2,3,7,7,4,5,5,6,7,7,6,7,6,7]
count = Counter(nos)                     # this Counter is an instance of the Counter class

print(str(count) + ' :  ')

three_most_common = count.most_common(3)
print(three_most_common)
