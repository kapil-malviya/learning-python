# Modules : [01]


"""
=>> A group of functions, variables and classes saved to 
	a file, which is nothing but module
=>> Every Python file (.py) acts as a module (mymodule.py)
=>> A group of modules is Package
=>> A group of packages is Library

"""


"""
Advantages of modules : 
=>> code reusability
=>> readability
=>> maintainability (easy to maintain)

"""

"""
Various possibilties of import:
=>> import modulename
=>> import module1,module2,module3
=>> import module1 as m        =>> aliasing 
=>> import module1 as m1,module2 as m2,module3

=>> from module import member
=>> from module import member1,member2,memebr3
=>> from module import memeber1 as x
=>> from module import *

"""


'''
Reloading a Module:
=>> By default module will be loaded only once 
	eventhough we are importing multiple times. 

imp module =>> 
	from imp import reload
	reload(module_name)

dir() function =>> 
	to check other functions/variables or members 
	in imp module

'''