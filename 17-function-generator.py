# Generator : 

'''
def firstn(num):
	n=1
	while n<=num:
		yield n
		n=n+1
values=firstn(100)
for x in values:
	print(x)
'''


# generate fibonacci numbers : (fibonacci = sum of previous two numbers)

def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
f = fib()
for x in f:
	if x>1000:
		break
	print(x)
	#print(x,end=',')


'''
Advantages of Generator function : 
=>> very easy to use
=>> memory utilization improved
=>> ** performance will be improved
=>> best suitable for reading data from large number of files
=>> web scraping and web crawling concept

'''