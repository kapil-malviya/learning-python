# given no. is odd or even number :

'''
def evenodd(n):
	if n%2==0 :
		print('{} is even number.'.format(n))
	else:
		print('{} is odd number.'.format(n))
evenodd(88)
evenodd(89)
# evenodd(int(input('enter number : ')))
'''


# factorial of a given number : 
'''
def fact(n) :
	result = 1
	while n>=1 :
		result=result*n
		n=n-1
	return result
print(fact(5))
for i in range(1,6):
	print('factorial of {} is : {}'.format(i,fact(i)))
'''


# multiple parameters : 

'''
def sum_sub(a,b):
	sum = a+b
	sub = a-b
	return sum,sub

c,v=sum_sub(100,50)
print('the sum : ',c)
print('the sub : ',v)

'''


def calc(a,b):
	sum = a+b
	sub = a-b
	mul = a*b
	div= a/b
	return sum,sub,mul,div

t = calc(88,18)
print('results : ',t)      # =>> (106, 70, 1584, 4.888888888888889) =>> tuple form
# print(round(t[3],2))     # =>> 4.89
# print(round(t[3]))       # =>> 5
for xx in t :
	print(xx)
print(type(t))             # =>> <class 'tuple'> =>> default return type

