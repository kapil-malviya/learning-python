# Type casting or Type coersion or Type conversion
	# from one type of data type to another type of datatype
#  int(anytype to int)  float(... to float)  complex(..to complex)  str(..to string datatype)

# bool()  
  # 0 (zero) = False
  # 1/5/0.8 (non zero) = True

# passing argument in int value
a=0
a1=1
a2=10
a3=101
a4=-20
print(bool(a))   # False
print(bool(a1))  # True
print(bool(a2))  # T
print(bool(a3))  # T
print(bool(a4))  # T
print()

# passing argument in float value
b=0.0
b1=0.8
b2=88.18
b3=-8.8
print(bool(b))   # F
print(bool(b1))  # T
print(bool(b2))  # T
print(bool(b3))  # T
print()

# passing argument in complex 
# if both real and imaginary part are zero(0) only then it returns False 
# otherwise True

c=18+8j
c1=0+0j
c2=18.8+0j
print(bool(c))   # T
print(bool(c1))  # F 
print(bool(c2))  # T
print()

# on passing string argument :
  # if the string is empty then only it will return False,   
  # even if the string consider space it will return True ...

d="8"
d1="8.8"
d2="eight"
d3="0"
d4=" "
d5=''
print(bool(d4))  # T
print(bool(d5))  # F
print(bool(d3))  # T
print(bool(d1))  # T
print(bool(d2))  # T
print(bool(d))   # T
print()
print()

# on passing binary, octal and hexa-decimal value

e=0b000         #binary
e1=0b1001
f=0o00          #octal
f1=0o1
g=0x00          #hexa-decimal
g1=0X88
print(bool(e))   # F 
print(bool(e1))  # T
print(bool(f))   # F
print(bool(f1))  # T
print(bool(g))   # F
print(bool(g1))  # T