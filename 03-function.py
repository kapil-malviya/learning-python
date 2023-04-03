##  types of arguments : 

"""
def ff(a,b):    =>> formal parameters
	body
ff(80,88)       =>> actual arguments
    =>> [a,b is parameters]
    =>> [80,88 is arguments]


Multiple types of Actual arguments : 
- positional, keyword, default, variable length arguments
"""

# positional arguments : (positional order) : order & no. of argument both imp..

def sub(a,b) :
	print(a-b)
                               
sub(100,50)      #  =>> 50   
sub(50,100)      #  =>> -50  =>> order is important



# keyword argument : (passing argument by parameter name) : order not imp.. but no. of arguments imp..

def wish(name,msg) : 
	print('hello..',name,msg)

wish(name='kapil,',msg='acc debited by 1.5cr')      # =>> hello.. kapil, acc debited by 1.5cr
wish(msg='acc credited by 2.8cr',name='kapil,')     # =>> hello.. kapil, acc credited by 2.8cr

#wish(msg='good evening','kapil,')   # =>> invalid =>> SyntaxError: positional argument follows keyword argument
wish('kapil,',msg='good evening')    # =>> valid : hello.. kapil, good evening     



# default argument :   default argument must be last argument only


def wish(name='guest') :
# def wish(naam='guest',kaam='xx'):                  => Valid                   
# def wish(name,msg="Good Morning"):                 => Valid              
# def wish(name="Guest",msg):                        => Invalid                   
# def wish(age, kaam, name="Guest",msg='xcvcx'):     => Valid 
	print('hey',name,'good evening..')
wish()             # =>> hey guest good evening..
wish('kapil')      # =>> hey kapil good evening..
wish('xx')         # =>> hey xx good evening..
print()
print()


def wishh(age, marks, naam='guest', kaam='xyz') :
	print('name : ',naam)
	print('age : ',age)
	print('marks : ',marks)
	print('kaam : ',kaam)

wishh(28,88,'kapil','xx')
print()
wishh(28,marks=89,naam='kapilmalviya')      # =>> positional argument must be first
