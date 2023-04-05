'''
Anonymous function :  

	=>> declaring function without name / nameless functions

it's use/requiremen :
    =>> if we've requirement of instant use (only one time usage)

lambda : used to define anonymous function

Syntax : 
	lambda input:expression

'''

# lambda n:n*n

s = lambda n:n*n
print(s(4)) 
print(s(5)) 
print(s(8),'\n') 


# find sum of given two numbers :

w = lambda a,b : a+b  
# print(w(8,8))
print('the sum of {} and {} is : {}'.format(8,88,w(8,88)))
print('the sum of {} and {} is : {}'.format(88,83,w(88,83)))
print('the sum of {} and {} is : {}'.format(808,880,w(808,880)),'\n')


# find biggest of given two values :

q = lambda a,b : a if a>b else b
print('the biggest of {} and {} is : {}'.format(800,808,q(800,808)))
print('the biggest of {} and {} is : {}'.format(88,83,q(88,83)))


###  passing function as an argument to another function :  lambda expression is best choice 
""" 
 =>> these are inbuilt functions :

filter()             : these functions always             
map()                  expects another function
reduce()               as an argument

Syntax : 

filter(function,sequence)
map(function,sequence)
reduce(function, sequence)

"""

## filter() =>> if fun. is true, it'll consider element from sequence & if false, ignore the rest element

def iseven(x) : 
	if x%2==0 :
		return True
	else: 
		return False
l = [0,3,8,87,89,88,82,80]
# filter(iseven,l)
l1 = list(filter(iseven,l))
print(l1)                         # =>> [0, 8, 88, 82, 80]
print()

# orr 

l = [0,3,8,87,89,88,83,82,80]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)                         # =>> [0, 8, 88, 82, 80]

l2 = list(filter(lambda x:x%2!=0,l))
print(l2)                         # =>> [3, 87, 89, 83]
print()


### map()  =>> generate new element with the required modifications


def double(x):
	return x*2
l = [1,2,3,4,5]
l1 = list(map(double,l))
print(l1)                    # =>>  [2, 4, 6, 8, 10]


l = [1,2,3,4,5]
l1 = list(map(lambda x:x*2,l))
print(l1)                    # =>>  [2, 4, 6, 8, 10]


# multiple sequence : map()

l1 = [1,2,3,4,5]
l2 = [8,18,80,88,0]
l3 = list(map(lambda x,y : x*y,l1,l2))
print(l3)                   # =>>  [8, 36, 240, 352, 0]


l4 = [1,2,3,4,5,6,7,8,9]             # =>> xtra values will be ignored
l5 = ['a','z','x','e','s']
l6 = list(map(lambda x,y : x*y, l4,l5))
print(l6)                   # =>> ['a', 'zz', 'xxx', 'eeee', 'sssss']



### reduce() =>> reduce function reduces sequence of element to single element by appling specified function
# Syntax : reduce(function, sequence)
# s = [10,30,50,60,70,80]    =>> 
"""  reduce(function) by default not available in python, ofcourse it's inbuilt function but present inside 
		a functools (module), we requiew to import this module, then only we can use reduce(function)

     ->> so below code won't work ;

ll = [10,30,50,60,70,80]
result = reduce(lambda x,y : x+y, ll)
print(result) 
"""
