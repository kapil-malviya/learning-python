#   Working with random module:  
'''
3. uniform(x,y)
	=>> this function always generate 
        between x and y (x & y not inclusive)
        it generates float values
'''


'''


from random import *
for x in range(13) :
	print(uniform(3,8))

'''



'''
5.912775910262907
3.992964570300149
6.505329936383763
3.523986842645603
7.448238751754014
6.196667282455849
3.4283457020216304
5.531075900003348
7.827034689084079
6.705914971585473
6.1991890624079105
6.006730826043753
6.6301032953963155

'''

'''
4. randrange(start, stop, step)
	=>> returns a random number from the range

	start <= x < stop

	=>> start is inclusive 
	=>> stop is exclusive

randrange(10)     =>> generate number from 0 to 9
randrange(1,10)	  =>> generate number from 1 to 9
randrange(1,10,2) =>> generate number 1, 3,5,7,9


'''

"""

from random import * 
for x in range(10) :
	print(randrange(10))

3
1
3
0
1
7
3
5
7
5 		


from random import *
for x in range(10) :
	print(randrange(1,10))


1
4
5
9
2
9
9
7
7
5 			"""



from random import *
for x in range(10) :
	print(randrange(1,10,2))

'''
9
1
3
1
7
7
5
9
5
7 		'''