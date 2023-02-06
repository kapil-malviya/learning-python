# Relational or Comparison operators
# ==, !=, >, <, >=, <= 


a=188
a1=18
a2=28.8
a3=18+4j
a4=True
a5=0b11011
a6=0o11011
a7=0x11011
a8='kapil'
a9='malviya'
a10='honda'
a11='Honda'     # honda > Honda > HONDA
a12='HONDA'
a13='harsh'     # a<b<c<d<e<f......<z
a14='hursh'

print('a>a1 = ',a>a1)    # True
print('a>=a1 = ',a>=a1)  # True
print('a<a1 = ',a<a1)    # False
print('a<=a1 = ',a<=a1)  # False
print('a==a1 = ',a==a1)  # False
print()

print('a2>a4 = ',a2>a4)   # T
print('a4>a6 = ',a4>a6)   # F
# print('a7>a9 = ',a7>a9) wont support with string
print('a8>a9 = ',a8>a9)   # F
print('a9>a10 = ',a9>a10) # T
print('a8==a10 = ',a8>a10) # T
                           # string value consider alphabetical order while comparision
print()

print('a10==a11 = ',a10==a11)   # F
print('a11==a12 = ',a11==a12)   # F
print()

print('a10>a11 = ',a10>a11)    # T
print('a10>a12 = ',a10>a12)    # T
print()

print('a10<a11 = ',a10<a11)    # F
print('a10<a12 = ',a10<a12)    # F
print()

print('a11>a12 = ',a11>a12)   # T
print('a11<a12 = ',a11<a12)   # F
print()

print('a13==a14 = ',a13==a14)  # F
print('a13<a14 = ',a13<a14)    # T
print('a13>a14 = ',a13>a14)    # F
print()

if (a14>a13):
	print("'hursh' is greater than 'harsh'")
else :
	print("'harsh' is greater than 'hursh'")

print()


print(a4<a1<a2<a>a5)  # T  (all conditions must be true)
print(a4>a1<a2<a>a5)  # F  (even if one condition is false then it will return false)
print()

b=88
c=80+8
d=44*2
e=176/2
f=98-8
g=88.0


print(b==c==d==e==g!=f)  # T
print()

print(0b1111==0o1111==0x1111)  # F