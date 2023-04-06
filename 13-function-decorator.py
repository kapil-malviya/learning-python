# decorator : double or multiple decorator ;


###   decorator chaining :

'''
def decor(func):
	def inner(name):
		print('first decor function execution...')
		func(name)
	return inner

def decor1(func):
	def inner(name):
		print('second decor function execution...')
		func(name)
	return inner


@decor
@decor1
def wish(name):
	print('hello..',name,'good evening.')	

wish('kapil')
print('\n\n')
'''




def decor1(func):
	def inner():
		x = func()
		return x*x
	return inner

def decor(func):
	def inner():
		x = func()
		return x*2
	return inner

"""
@decor           #  inner decor (decor1) executed first 
@decor1          #   & then outer decor(decor) executed              
"""

@decor1       # here inner decor(decor x*2) executed first & 
@decor        #  then outer decor(decor1) executed


def num():
	return 10

print(num())    

 # =>> 200 (10*10 => 100*2)
 # =>> 400 (10*2  => 20*20)