# while loop 
#          ( factorial of a number )



# val=int(input("Enter no. : "))
# fact=1
# i=1
# while i<=val :
# 	fact=fact*i
# 	i+=1
# print('The factorial of {} is {}'.format(val,fact))


val=int(input("Enter no. : "))
if val<0 :
	print('Factorial are not defined for a negative value ')
else :
	fact=1
	i=1
	while i<=val :
		fact=fact*i
		i+=1
	print('The factorial of {} is {}'.format(val,fact))
