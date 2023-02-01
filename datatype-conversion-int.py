# Type casting or Type coersion or Type conversion
	# from one type of data type to another type of datatype
#  int(anytype to int)  float(... to float)  complex(..to complex)  str(..to string datatype)

# int()
a=123.456  # float value
b=10+20j   # complex value
c=True     # boolean value
d=False    #   ---
e="10"     # string value
f="10.2"   #   ---  
g="10 k"   #   ---
h=0b11001  # binary value
i=0o11001  # octal value
j=0x11001  # hexa-decimal value


print(int(a)) # -> 123 (output)  this is int value
# print(int(b)) can't convert complex to int
print(int(c))  # -> 1
print(int(d))  # -> 0
print(int(e))  # ->10
#print(int(f))  # when converting string value to int value, compulsory.. 
#print(int(g))  # that string should contain only int value 
                # always expect value in base - 10 only  
print(int(h))  # -> 25         
print(int(i))  # -> 4609
print(int(j))  # -> 69633