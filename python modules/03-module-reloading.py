# Reloading module : 

'''
import time
import demomodule2

print('program entering into sleeping state for 45 seconds..')

time.sleep(45)

import demomodule2
print('imported module loaded only once even after updating it during the time span of 45 seconds..')
'''

""" =>>
		This is from demo module 2...
		program entering into sleeping state for 45 seconds..
		imported module loaded only once even after updating it during the time span of 45 seconds..	
"""




# now, we need updation of module during its run time :

# imp module
# reload()


import time 
from imp import reload
import demomodule2

print('program entering into sleeping state for 38 seconds..')

time.sleep(38)
reload(demomodule2)
print('via reload(module) function imported module loaded again, after updating it during the time span of 38 seconds..')

''' =>> 
		This is from demo module 2 ...
		program entering into sleeping state for 38 seconds..
		This is from demo module 2  by kapill...
		via reload(module) function imported module loaded again, after updating it during the time span of 38 seconds..
'''
