# Immutable vs fundamental datatypes(int,float,bool,complex,string)  
# immutable => non changeable  &  mutable => changeable  

# all fundamental datatypes are immutable, means.. once object created, changes can't be performed   
# if we tried then new object created 

# if the same content required repeatedly, not recommended to create separate object, it creates   
# only one object and all the refrences are going to be shared

    # to check this refrences, check the address of object by id() method or ^is^ operator



a=10        # the address of a,b & c will be same and will be different from cx
b=10
c=10         # output => 140736520447048 => address of internal object
# one object = 10,, three refrences=a,b,c
cx=18
d='ind'        # address d,e = same
e='ind'
f='india'

 # id = address of variable

print(id(a))    
print(id(b))
print(id(c))
print(id(cx))
print(id(d))
print(id(e))
print(id(f))
print()

#  is operator (output in boolean)

print(a is b)  # True
print(b is a)  # T
print(a is c)  # T
print(a is cx)  #False
print()


a1=256
a2=256    # in int value, applicable upto 256, 256< it will return False >> have to check in latest update
a3=257
a4=257
a5=-5
a6=-5  
a7=-6
a8=-6
print(id(a3))
print(id(a4))
print(a1 is a2)  # T
print(a3 is a4)  # T (shell is returning false)
print(a5 is a6)  # T
print(a7 is a8)  # T (shell is returning false)
print()


# for float and complex values 
b1=10.8
b2=10.8
c1=8+18j
c2=8+18j
d1=True
d2=True
print(b1 is b2)  # T  (shell is returning False)
print(c1 is c2)  # T  (shell is returning False)  >> check updates whether applicable or not in latest version of python
print(d1 is d2)  # T


# by this performance and memory utilisation will be improve