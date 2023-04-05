### Nested functions : function inside a function ;


def outer():
	print('outer function started/ executed..')
	def inner():
		print('inner function executed..')
	inner()
outer()

# return =>> 
# outer function started/ executed..
# inner function executed..

"""  requirement of nested function :
 soo.. if a group of statements inside a function repeatedly 
   required, then these group of statements i'll define as inner function
   and i can call that inner function directly without writing these 
   lines again & again.. """


def f1():
	def inner(a,b):
		print('sum : ',a+b)
		print('average : ',(a+b)/2)
	inner(808,888)
	inner(80,800)
	inner(82,88)
	inner(83,88)
f1()

"""  =>> 
	sum :  1696
	average :  848.0
	sum :  880
	average :  440.0
	sum :  170
	average :  85.0
	sum :  171
	average :  85.5
"""

print()


def outer():
	print('outer function started..')
	def inner():
		print('inner function executed..')
	print('outer function returning inner function..')
	return inner
f1 = outer()
"""
		outer function started..
		outer function returning inner function..
"""
print()

f1()
"""
		inner function executed..
"""

print()
print(f1())
"""
		inner function executed..
		None
"""