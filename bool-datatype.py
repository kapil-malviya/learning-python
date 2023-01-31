a=20
b=30
c=a<b       # true
d=a>b       # false
e=True
f=False

print(c)
print(d)

print(type(e))
print(type(f))

                           # True = 1
                           # False = 0
a1=True+True
print("True + True = ", a1)    # output = 2

a2=True
a3=a1+a2
print("True + True + True = ", a3)    # output = 3

a4=False
print("True + True + False = ", a1+a4)   # output = 2
print("False + False = ", a4+a4)   # output = 0
print("True + False = ", a2+a4)   # output = 1