# Function Decorators : 

"""
	Decorator is a function which can take a function as argument and extend its functionality
	and returns modified function with extended functionality

Input function ==> Decorator function ==> Output function with extended functionalities

"""


def wish(name):
	print('hello...',name,'good evening...')
wish('aaa')
wish('zzz')
wish('xxx')
print('\n\n')




def decor(func): 
	def inner(name): 
		if name=='dollar':
			print('we need dollars worth $88 Billion')
		else :
			func(name)
	return inner

@decor      # by stating this, above function will be executed internally, decor will always going 
            #  to execute while calling function, if we remove decor only wish fun. will execute
def wishh(name):
	print('we need 88 tons of',name)

wishh('silver')         # =>> we need 88 tons of silver
wishh('gold')           # =>> we need 88 tons of gold
wishh('dollar')         # =>> we need dollars worth $88 Billion      
wishh('dollars')        # =>> we need 88 tons of dollars
print('\n\n')





def decor(func): 
	def inner(name): 
		if name=='dollar':
			print('we need dollars worth $88 Billion')
		else :
			func(name)
	return inner

def wishh(name):
	print('we need 88 tons of',name)

decorfunction = decor(wishh)

wishh('dollar')                  # =>> we need 88 tons of dollar
decorfunction('dollar')          # =>> we need dollars worth $88 Billion

wishh('gold')                    # =>> we need 88 tons of gold
decorfunction('gold')            # =>> we need 88 tons of gold
