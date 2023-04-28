# using function f1() which is in module1.py file present in pack1 folder
# no need of making  __init__.py  file

'''
import pack1.module1
pack1.module1.f1()
 

or =>>

'''


from pack1.module1 import f1
f1()




'''
=>> output

	this is from module1 present in pack1..

'''