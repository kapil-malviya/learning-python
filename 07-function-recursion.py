'''
Recursive function :

=>> A function that calls it self recursive function

factorial(4) = 4*factorial(3)
             = 4*3*factorial(2)
             = 4*3*2*factorial(1)

=>> reduce the length of the code & improve readability
=>> solve complex problems with the help of recursion
'''

# factorial function by using recursion : 

def factorial(n) :
	if n==0 :
		result = 1 
	else :
		result = n*factorial(n-1)
	return result

print(factorial(0))
print(factorial(5))
print(factorial(6))