# for loop 

# factorial

#  factorial sirf +ve int. ka hi nikalega

val=int(input('Enter number for a factorial value : '))
fact=1
for i in range(1,val+1):
	fact=fact*i
	# print(fact) => 1, 2, 6, 24, 120, 720... ( will print different values )
print('Factorial of a number {} is {}'.format(val,fact))