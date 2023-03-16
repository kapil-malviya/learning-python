#  list aliasing & cloning

# shallow copy  => both are pointed to the same object  

'''
x = [10,18,28,8]
y = x                         ## aliasing
y[1] = '888'                 
print(id(x) , id(y))            # =>> same id
print(x,'\n')                   # =>> [10, '888', 28, 8]
'''


'''
   deep copy  => different object (cloned object)
   =>> create cloned object by two ways : 
     a. By using Slice Opertator
     b. By using copy method 
     =>> advantage : maintain backup for future reference

'''

x = [10,18,28,8]
y = x[:]
y[1] = '888'
print(x)                           # =>> [10, 18, 28, 8]
print(y)                           # =>> [10, '888', 28, 8]
print(id(x) , id(y) , '\n')        # =>> different id

#     orr

a = [10,18,28,8]
b = a.copy()
b[1] = '8888'
print(a)                              # =>> [10, 18, 28, 8]
print(b)  # cloned /complete different object =>> [10, '8888', 28, 8]