"""
Working with random module:
	this module defines several functions to generate random numbers, 
	 =>> games, otp, captcha


1. random()
	=>> this function always generate 
        between 0 and 1 (not inclusive)

		0 < x < 1

	=>> always different output
"""

"""
from random import *
for i in range(10):
	print(random())
 
 return =>>
0.969236734293572
0.4075563103199199
0.059872046665064405
0.7591577793863499
0.3051553165793839
0.05635712908173807
0.432430115082463
0.3599141193063642
0.17929658232611
0.8317125724774489
"""



"""
2. randomint(1,100)
	=>> this function always generate 
        between 1 and 100 (1 & 100 inclusive)

"""


from random import *

for  x in range(28):
	print(randint(1,100)) 

print()

for xx in range(10):
	print(randint(7,13))


""" =>> output
9
11
13
8
12
12
10
10
7
12

"""