'''    the special variable  __name__  =>> 

two ways to execute module =>> (either directly or from another program)
1. directly execute module
2. indirectly use of that module as a dependent program 
	(importing this module to another module & then execution..)


if __name__ == __main__
  : then the code executed directly as a program 

'''



def f1():
	if __name__ == '__main__' :
		print('the code executed directly as a program..')
		print('the value of __name__ : ', __name__)
	else : 
		print('the code executed indirectly as a module from some other program..')
		print('the value of __name__ : ', __name__)
f1()


"""

the code executed directly as a program..
the value of __name__ :  __main__

"""