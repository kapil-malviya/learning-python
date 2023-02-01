# Type casting or Type coersion or Type conversion
	# from one type of data type to another type of datatype
#  int(anytype to int)  float(... to float)  complex(..to complex)  str(..to string datatype)

# float()

a=123      # int value
b=10+20j   # complex value
c=True     # boolean value
d=False    #   ---
e="10"     # string value
f="10.2"   #   ---  
g="ten"    #   ---
h=0b11001  # binary value
i=0o11001  # octal value
j=0x11001  # hexa-decimal value


print(float(a))  # -> 123.0 (output)  this is int value
# print(float(b)) can't convert complex to float and int type
print(float(c))  # -> 1.0
print(float(d))  # -> 0.0
print(float(e))  # -> 10.0
print(float(f))  # -> 10.2

#print(float(g))  # while converting string value to float value, compulsory.. 
                  # that string should contain only int or float value 
                  # and should be specified using base - 10 only 

print(float(h))  # -> 25.0         
print(float(i))  # -> 4609.0
print(float(j))  # -> 69633.0