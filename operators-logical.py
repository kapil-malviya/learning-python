# Logical operators (and, or, not)
 
#  for boolean types
   # and => if both arguments are True
   # or => if atleast one argument is True
   # not => opposote

#  for non boolean types
   # 0 means False
   # non zero means True
   # empty string ("") False
   # space in string (" ") will be considered as True

a1=True
a2=False
a3=0
a4=8
a5=88
a6='kapil'
a7=''      # empty string
a8=' '

 # for boolean

print(a1 and a2)     # F
print(a1 and a1)     # T  (both must True)
print()

print(a1 or a2)      # T  (atleast one argument is True)
print()

print(not a2)        # T
print(not a1)        # F   (opposite)
print()

 # non boolean

 # x and y   # if x (first-one) is False return x (x is answer)
             # if x (first-one) evaluates as True return Y (y is answer)

print('0 and 8 = ',a3 and a4)    # 0
print('88 and 0 =',a5 and a3)    # 0
print('8 and 88 =',a4 and a5)    # 88
print('88 and 8 = ',a5 and a4)   # 8


print("8 and 'kapil' = ",a4 and a6)    # kapil
print("'kapil' and 8 = ",a6 and a4)    # 8
print()


# x or y
       # if x is evaluates to True then return x 
       # if x evaluates to False then return y

print('8 or 88 =',a4 or a5)       # 8
print('0 or 8 = ',a3 or a4)       # 8
print('88 or 0 =',a5 or a3)       # 88
print('88 or 8 =',a5 or a4)       # 88
print('0 or 0 = ',a3 or a3)       # 0
print('0 or True = ',a3 or a1)    # True
print()

 # not x
       # if x is True returns False
       # if x is False returns True
print(not a7)   # T
print(not a4)   # F