### functions : 

'''
  -> code reusability
  -> two types : 
     - predefined/inbuilt functions
     - user defined functions

# syntax for function : 

def function_name(parameters):
	logic
	return result
'''


"""

def wish():
	# this function is just to implement wish functionality
	print('kapil')
	print('delhi')
	print('gold')
wish()
print()	
wish()


# function with parameter :

def wish(naam):
	print("Hello {}, How's you?".format(naam))

wish(8)
wish('kapil')
wish('kapilmalviya')


# square of a number :


def square(x):
	print('square of {} is : {}'.format(x,x*x))

# square(int(input('enter value : ')))
square(18)
square(88)



#  adding two numbers : 

def add(a,b) :
	x=a+b
	print(a,'+',b,'=',x)

add(10,88)



def add(a,b) :
	return a+b

result = add(10,20)
print('sum is : ',result)
print('sum is : ',add(88,888))



def f1():
	print("hey..")

f1()               # =>> hey..
print(f1())        # =>> hey..  =>> None

"""


def f1():
	print('hello kapil')
	return 5             # function terminated here
	print("hii")         # won't consider anything (anyvalue) after return

f1()                # =>>  hello kapil
a = f1()            # =>>  hello kapil
print(a)            # =>>  hello kapil  followed by  None (bcoz not returning any value)
# print(f1())       # =>>  hello kapil  followed by  None (bcoz not returning any value)
