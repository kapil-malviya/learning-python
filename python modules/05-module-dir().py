# dir() : Finding members of module by using dir() function ;
#       : we'll get list of current module members


import demomodule4

dir(demomodule4)
print(dir(demomodule4))


""" =>> 

		['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', 
		'__loader__', '__name__', '__package__', '__spec__',
		 'f1', 'f2', 'x', 'y', 'z']
"""



print('annotations : ',__annotations__)   # =>> {}
print('builtins : ',__builtins__)      # =>> <module 'builtins' (built-in)>
print('cached : ',__cached__)          # =>> None
print('doc : ',__doc__)                # =>> None
print('file : ',__file__)              # =>> C:\Users\Dell\Desktop\python\Modules\05-module-dir().py
print('loader : ',__loader__)          # =>> <_frozen_importlib_external.SourceFileLoader object at 0x0000017FD5683D50>
print('name : ',__name__)              # =>> __main__
print('package : ',__package__)        # =>> None
print('spec : ',__spec__)              # =>> None
print('f1 : ',demomodule4.f1)          # =>> f1 :  <function f1 at 0x0000021B12C59DA0>
print('f1 : ',demomodule4.f1())        # =>> hello kapil...     =>>   f1 :  None 
print('f2 : ',demomodule4.f2())        # =>> have some gold     =>>   f2 :  None
print('x : ',demomodule4.x)            # =>> x : 80
print('y : ',demomodule4.y)            # =>> y : 88
print('z : ',demomodule4.z)            # =>> z : 800



