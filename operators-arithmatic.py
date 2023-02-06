# operators in python

# Arithmatic operators (+,-,*,**,/,//,%)    (// => floor division python special )
                                        #   (** => exponential or power operators python special )
# Relational or Comparison operators 
# Logical operators
# Bitwise operators
# Assignment operators
# Special operators


a=88
b=18
c=2
d=10.8

print("a+b = ",a+b)
print("a-b = ",a-b)
print("a*b = ",a*b)
print("a/b = ",a/b)    # always return float value
print("a//b = ",a//b)  # floor division (return=4)
print("a%b = ",a%b)    # remainder
print("b**c = ",b**c)  # a power b 
print()

print("d/c = ",d/c)     # return => 5.4
print("d//c = ",d//c)   # return => 5.0 (if argument is in int type, it will return int value)
print("a//d = ",a//d)   # return => 8.0 (if the  argument is in float type, it will return float value)
                        #        (return nearest int value in float type)
print()

print("d**c = ",d**c)   # return float value
print()
print()

  #   + operator also applicabe for string type 
   #    in this case it is considered as string concatenation operator 
   # for this both values should be string type only

e='kapil'
f="malviya"
g=8
h=-3
i=0

print("e+f = ",e+f)
print()

#  * operator 
  #  one value should be string and another value should be int type only to get repetition of that string  

print("e*g = ",e*g,'\n','\n')
print('g*f = ',g*f,'\n')
print("g**h = ",g**h)
print("g**i = ",g**i)
print("e*i = ",e*i)    # wont print 'kapil'

#  x/0   x%0   x//0
#  return zero division error