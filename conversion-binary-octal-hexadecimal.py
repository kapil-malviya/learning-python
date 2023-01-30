a=888       # simple (decimal form )
x=0b1111    # binary form
y=0o1237    # octal form
z=0x8888    # hexa-decimal form

# bin() function is used to convert any form to the binary form

print(bin(a))      # decimal to binary 
print(bin(y))      # octal to binary 
print(bin(z))      # hexa-decimal to binary

# oct() function is used to convert any form of int type no. to octal form

print(oct(a))    # base 10 to 8
print(oct(x))    # base 2 to 8
print(oct(z))    # base 16 to 8

# hex() is used to convert any form to the hexa-decimal form int type

print(hex(a))   # 10 to 16
print(hex(x))   # 2 to 16
print(hex(y))   # 8 to 16

