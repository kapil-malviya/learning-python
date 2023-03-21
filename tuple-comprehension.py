# tuple comprehension

"""
li = [x*x for x in range(1,11)]
print(li)
"""

"""  tuple comprehension is not supported in python
"""

tuple1 = (x*x for x in range(1,11))
print(tuple1)            # =>> <generator object <genexpr> at 0x000002680C1C42B0>
print(type(tuple1))      # =>> <class 'generator'>

for x in tuple1 :        # =>> this is not a tuple object but a generator object    
	print(x)                



###  program to take a tuple of numbers from the user & print sum & average

t = eval(input("Enter some tuple of numbers : "))
l = len(t)
sum = 0
for xx in t :
	sum=sum+xx
print("the sum : ",sum)
print('the average : ', sum/l)