# Reloading module : module will be loaded only once

'''
import demomodule1
import demomodule1
import demomodule1
import demomodule1
import demomodule1
import demomodule1

print('module loaded only once..')
'''

""" =>> imported module 6 times but loaded only once 

		This is from demo module...
		module loaded only once..
"""



import demomodule1
import demomodule1
print('module loaded only once..')
import demomodule1
import demomodule1
import demomodule1
import demomodule1
print('module loaded only once..')

''' =>> 
		This is from demo module...
		module loaded only once..
		module loaded only once..

'''

