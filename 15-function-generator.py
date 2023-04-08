### Generator : if we want to represent a group of values without storing values in memory 



def countdown(num):
	print('start countdown')
	while(num>0):
		yield num
		num=num-1
values=countdown(5)
print(countdown(5))
print(values)
for x in values :
	print(x)    

'''
# here not a single value will be stored in a memory



def mygen():
	yield 'A'
	yield 'B'
	yield 'C'
	yield 'D'

g = mygen()
for x in g:
	print(x)

print(type(g))      # =>> <class 'generator'>
# print(next(g))      # =>> A
# print(next(g))      # =>> B
# print(next(g))      # =>> C




'''