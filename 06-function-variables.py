#  Variables : 
'''
Types : Global & Local Variable

Global Variable : outside of function ;
Local Variable : Inside of a function ;



a = 88
def xx():
	print('a = ',a)

def xy():
	print('a = ',a)

xx()         #  =>> a =  88
xy()         #  =>> a =  88



def xz():
	a = 10
	print('a = ',a)

def xc():
	print('a = ',a)

xz()          #  =>>  10
# xc()        #  =>>  NameError: name 'a' is not defined

'''

"""
a = 88
def x1():
	a = 777
	print('a = ',a)

def x2():
	print('a = ',a)

x1()       # =>> 777
x2()       # =>> 88
"""
#  priority :  local > global

'''
a = 88
def x1():
	global a           # consider this as global variable / making it available for all functions
	a = 777
	print('a = ',a)

def x2():
	print('a = ',a)

x1()       # =>> 777
x2()       # =>> 777
'''

"""
def z1():
	global a 
	a = 888
	print('a : ',a)
def z2():
	global a
	a = 999
	print('a : ',a)
def z3():
	print('a : ',a)
 
z1()       # =>> 888
z2()       # =>> 999
z3()       # =>> 999
print()

z2()       # =>> 999
z1()       # =>> 888
z3()       # =>> 888
"""


# want global variable value inside a function if local variable is also there


a = 88
def f1():
	a = 98
	print(a)                #  =>> 98
    #print(globals())       #  =>> returns dictionary
	print(globals()['a'])   #  =>> 88  (taking global variable)

f1()