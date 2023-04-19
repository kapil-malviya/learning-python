# importing demomodule5

'''    the special variable  __name__  =>> 

two ways to execute module =>> (either directly or from another program)
1. directly execute module
2. indirectly use of that module as a dependent program 
	(importing this module to another module & then execution..)


if __name__ == __main__
  : then the code executed directly as a program 

'''


import demomodule5 

print("from '06-module-dir()' we are executing demomodule5  f1() ")
demomodule5.f1()



"""
the code executed indirectly as a module from some other program..
the value of __name__ :  demomodule5
from '06-module-dir()' we are executing demomodule5  f1()
the code executed indirectly as a module from some other program..
the value of __name__ :  demomodule5

"""