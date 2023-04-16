# Reloading module : (reloading 2 times)



import time 
from imp import reload
import demomodule3

print('program entering into sleeping state for 28 seconds..')

time.sleep(28)
reload(demomodule3)      # (make change in file demomodule3 to check results)
print('via reload(module) function imported module loaded again after updating it during the time span of 28 seconds..')

time.sleep(28)
reload(demomodule3)
print('again via reload() imported module (demomodule3) loaded again during the time span of 28 seconds..')


""" =>> 
		this is the first version...
		program entering into sleeping state for 28 seconds..
		this is the second version...
		via reload(module) function imported module loaded again after updating it during the time span of 28 seconds..
		this is the third version
		again via reload() imported module (demomodule3) loaded again during the time span of 28 seconds..

"""