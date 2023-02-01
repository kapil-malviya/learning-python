# Type casting or Type coersion or Type conversion
	# from one type of data type to another type of datatype
#  int(anytype to int)  float(... to float)  complex(..to complex)  str(..to string datatype)

# complex() = two ways/forms to convert any type to complex datatype
#    form-1 : complex(x)   => x+0j  (x argument passing will become only real part)
#    form-2 : complex(x,y) => x+yj  (x = real part, y = imaginary part of complex number) 
# called overloaded functions where method name is same but the arguments are different 

a=123      # int value
a1=88
b=18.88    # float value
b1=8.08
d=True     # boolean value
e=False    
f="10"     # string value
f1="8"
g="10.2"
g1="8.8"     
h="ten"    
i=0b11001  # binary value
j=0o11001  # octal value
k=0x11001  # hexa-decimal value

# form-1  passing one argument only

print(complex(a))  # 123+0j
print(complex(b))  # 18.88+0j 
print(complex(d))  # 1+0j
print(complex(e))  # 0+0j => 0j
print(complex(f))  # 10+0j
print(complex(g))  # 10.2+0j
# print(complex(h)) while converting string value to complex, compulsory that string should 
                  # contain only int or float value and should be specified using base - 10 only
print(complex(i))  # 25+0j
print(complex(j))  # 4609+0j
print(complex(k))  # 69633+0j

# form-2 passing two arguments

print(complex(a,a1))  # 123+88j
print(complex(a,b))   # 123+18.88j
print(complex(a,d))   # 123+1j
print(complex(a,e))   # 123+0j
# print(complex(a,f)) complex() second argument can't be string
# print(complex(a,g))
print(complex(a,i))   # 123+25j
print(complex(a,j))   # 123+4609j
print(complex(a,k))   # 123+69633j
print(complex(b,i))   # 18.88+25j
print(complex(d,j))   # 1+4609j 
print(complex(e,k))   # 0+69633j => 69633j
# print(complex(g,d))  complex() can't take second argument if the first argument is string
print(complex(g))     # 10.2+0j