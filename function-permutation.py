# permutation & combination :


def fact(x) :
	fact=1
	for i in range(1,x+1):
		fact=fact*i
	print('Factorial : ',fact)
	return fact

n = int(input("enter value : "))
r = int(input("enter value : "))
val = fact(n)/fact(n-r)
print(val)
