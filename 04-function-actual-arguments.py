"""
Multiple types of Actual arguments : 
- positional, keyword, default, variable length arguments
"""

# variable length argument : passing any no. of arguments 

def f1(*x) :
	print('variable length arg. function ')
f1()
f1(8)
f1(8,88)
f1(8,88,888)


	# print sum of given numbers : 

def sum(*x):
	rslt=0 
	for xx in x:
		rslt=rslt+xx
	print('sum : ',rslt)
sum()
sum(10,88)
sum(10,88,800)
sum(10,88,888,88)
sum(10,88,89,98,88)
print()

	# multiple parameters : 

def sum(name,*n):
	rslt=0
	for x in n :
		rslt=rslt+x
	print('the sum by {} is : {}'.format(name,rslt))

sum(88)                      # =>> 0
sum('kapil',88,88,88,88)     # =>> 352
sum(88,88)                   # =>> 88




def sum(*n,name):
	rslt=0
	for x in n :
		rslt=rslt+x
	print('the sum by {} is : {}'.format(name,rslt))

# sum(name='silver',88)   #  =>> invalid 

#  keyword argument must be in last

sum(88,name='silver')            # =>> valid
sum(8,88,8888,888,name=8008)     # =>> the sum by 8008 is : 9872
print()


#  passing multiple keyword argument : Keyword Variable length argument  =>>  fun(**x)


def display(**kwargs) :       # =>> internally it's dictionary
	print('record info..')
	for m,n in kwargs.items() :
		print(m,"-->",n)

display(name='kapil', marks=88, age=28, gf='her')
print()
display(name='kapil', wife1='her1', wife2='her2')
print()
display(name='anna', marks=888, age=88, gf='sheisfine')
