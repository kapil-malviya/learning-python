var1=888          # decimal form where base is 10 and value 0 to 9
var_2=0b1010      # binary form (base-2), value (0 &1)
var3_=0B0101      # binary form (base-2), value (0 &1)
_var4=0o3075      # ill seven only because the base of octal form is 8
_var5_=0O70077    # till seven only because the base of octal form is 8
__var6=0x88980    # hexa-decimal form where(base-16) & value (0-9, a-f/A-F) here no case sensitive
__var_7=0X88fabE  # hexa-decimal form where(base-16) & value (0-9, a-f/A-F) here no case sensitive
_8var_8=0xbae88   # hexa-decimal form where(base-16) & value (0-9, a-f/A-F) here no case sensitive

print(var1)
print(var_2)
print(var3_)                               # remember a way to represent all form of int value
print(_var4)                               # decimal, binary, octal and hexa-decimal form
print(_var5_)
print(__var6)
print(__var_7)
print(_8var_8)
print(type(var1))
print(type(var_2))
print(type(var3_))
print(type(_var4))
print(type(_var5_))
print(type(__var6))
print(type(__var_7))
print(type(_8var_8))