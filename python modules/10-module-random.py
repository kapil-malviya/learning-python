#   Working with random module:  

'''
4. choice()
	=>> it won't return random number but returns 
        random object from the collection

'''

"""

from random import *
listt = ['gold', 'money', 'dollars', 'silver']   # this may be tuple or list but not set(set doesn't support indexing)
for x in range(8) :
    # print(choice(listt))
    print(choice('dollars'))



gold
gold
money
money
dollars
gold
dollars
dollars

r
d
s
a
d
l
a
d

"""


# program to generate a 6 digit random number as otp :


from random import *
for x in range(2) :
    print(randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9), sep='')
    # print(randint(100000,999999)) =>> 


"""
303547
950767

"""  

"""
alphabets : 
chr(65, 66, 67.... 65+25 =>> int)
chr(65, 90)

"""

from random import *
for x in range(10) :
    print(chr(randint(65, 90)))


"""
B
D
V
A
T
B
L
Z
S
W

"""