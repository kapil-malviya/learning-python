# bytes datatype
 # bytes datatype represents the group of numbers (only integers) {just like an array}
  # bytes must be in range of (0, 256)
  # value more than 255 will give 'ValueError'
  # bytes datatype is immutable

abc=[8,18,45,28,88,188,255] # 255<__ => return ValueError
b=bytes(abc)

print(b)
print(type(b))
print(abc[0])
print(abc[-2])
print(abc[-5:-2])
for abc in b :
	print(abc)
print()
# b[1]=28  # can not alter/change because bytes datatype is immutable 
           # TypeError: 'bytes' object does not support item assignment


# bytes datatype and bytearray
  # both are same but the only difference is byte datatype is immutable and bytearray is mutable