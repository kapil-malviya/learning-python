## Decorators : another ;

'''
def division(a,b):
	return a/b 

print(division(88,11))      # =>> 8.0
print(division(88,8))       # =>> 11.0
print(division(88,0))       # =>> ZeroDivisionError: division by zero
'''




def smartdivision(func):
	def inner(a,b):
		if b==0 :
			print("we can't divide a no. with 0(zero)...")
		else:
			return func(a,b)
	return inner

@smartdivision
def division(a,b):
	return a/b 

print(division(88,11))        # =>> 8.0
print(division(88,8))         # =>> 11.0
# print(division(88,0))       # =>> ZeroDivisionError: division by zero
print(division(88,0))         #  we can't divide a no. with 0(zero)...   followed by  None
