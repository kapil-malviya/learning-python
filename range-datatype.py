# range  (numbers)
   # immutable  
   # float numbers is not applicable  
      # whereas boolean,binary,octal & hexa-decimal is applicable

a=range(5)
a1=range(18,44)
a2=range(3,31,3)

for i in range(-30,-2,3):
	print(i)
print("---")

for j in range(0x88,0x118):
	print(j)
print("---")

for k in range(0o123,0o143):
	print(k)
print("---")

for l in range(0b101,0b1101):
	print(l)
print("---")

for m in range(False,True):
	print(m)
print("---")

print(type(a))
print(a)
print(a1)
print(a2)

print("---")

for x in a1:
	print(x)
print("---")
print(a1[5])
print(a1[4:14]) # return will be in range => range(22,32)   









