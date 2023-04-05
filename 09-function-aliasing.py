"""
everything in python ia an object
int, bool, float
"""
def f1():
	print('goldd')
print(f1)
print(f1())
print(id(f1))

'''   " Function Aliasing "

	assigning different name to the existing function,
	this concept is called : Function Aliasing, : for the 
	 existing function we can give another name.. ex : 
'''


def wish(name):
	print('we want : ',name)

greeting = wish    # for the wish we're providing another name
                   # call function by both names (wish/greeting)
wish('$ dollars')     # =>> we want :  $ dollars
greeting('goldd')     # =>> we want :  goldd

print(id(wish))       # =>> 1807218150592    both fun. objects are same
print(id(greeting))   # =>> 1807218150592    bcoz both are pointing to same address


# if we delete one name (reference), still we can access with another name (reference) :

del wish
greeting(88)         # =>> we want :  88

# if we remove all(1/2/3..) references then only object will be removed

