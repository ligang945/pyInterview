a, b = 2, 3
min = a if a < b else b
print(min)


mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(mylist[-1])

import random
random.shuffle(mylist)
print(mylist)

mydict = {x: x**2 for x in range(5)}
print(mydict)
random.shuffle(mydict)
print(mydict)

# mytuple = (1, 2, 3)
# random.shuffle(mytuple)
# print(mytuple)


a = '1\r@ 3\n4	5;6,7\r\n8\r\n'.split()
print(a)
