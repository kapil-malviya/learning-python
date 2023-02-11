####   module

# math module 
   #   sqrt(),  ceil(),  floor(),  pow(x,y),  factorial(),
   #   gcd(),  pi,  sin(), cos()...



# import math

# print(math.sqrt(16))    # 4.0
# print(math.pi)          # 3.141592653589793


### aliasing  (creating alternative name)

# import math as m
# print(m.sqrt(256))     # 16.0
# print(m.pi)            # 3.141592653589793


### 

# from math import sqrt,pi

# print(sqrt(121))      # 11.0
# print(pi)


from math import *     # importing all the members present inside the math module

# print(sqrt(283))       # 16.822603841260722
# print(pi)
# print(pow(13,2))       #  13**2 => 169.0
# print(pow(18.8,2))     #  18.8**2 => 353.44000000000005

r=int(input('Enter radius : '))
area=pi*r**2
print('Area : ',area)


