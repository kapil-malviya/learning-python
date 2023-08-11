a=int(input("enter value a"))
b=int(input("enter value b"))
c=int(input("enter value c"))

x=a+b+c
smallest=a

if a>b:
	smallest=b
if b>c:
	smallest=c

z=x-smallest

print("z=:",z)
