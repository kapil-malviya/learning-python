'''
import mathmodule

print(mathmodule.x)
print(mathmodule.y)
print(mathmodule.z)

mathmodule.product(80,88)
mathmodule.add(80,88)




import mathmodule as mm          # =>> module name aliasing

print(mm.x)
print(mm.y)
print(mm.z)

mm.product(80,88)
mm.sub(80,88)




from mathmodule import x,y,add

print(x)
print(y)
# print(z)
add(88,98)
# product(10,8)



from mathmodule import *     # (*) =>> everything

print(x)
print(y)
print(z)
add(88,98)
product(10,8)

'''

# creating alias name for the members also :

from mathmodule import x as a, y as b, add as c, sub as d, square as e

print(a)
print(b)
c(80,86)
d(8008,88)
e(89)