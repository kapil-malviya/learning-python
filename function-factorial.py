'''
x=int(input('Enter value : '))
f=1
for i in range(1,x+1):
	f=f*i
print('Factorial : ',f)
'''



def fact(x) :
	fact=1
	for i in range(1,x+1):
		fact=fact*i
	print('Factorial : ',fact)
fact(5)
fact(7)
fact(6)
