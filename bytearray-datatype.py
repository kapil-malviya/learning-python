# bytearray datatype     (like bytes datatype)
 # bytearray datatype represents the group of numbers (only integers) {just like an array}
  # bytearray must be in range of (0, 256)
  # value more than 255 will give 'ValueError'
  # bytearray datatype is mutable (bytes datatype is immutable)  

abcd=[8,18,45,28,88,188,255] # 255<__ => return ValueError
bb=bytearray(abcd)


print(bb)
print(type(bb))
print(abcd[0])
print(abcd[-2])
print(abcd[-5:-2])
for abcd in bb :
    print(abcd)
print()

# bytearray datatype is mutable

bb[2]=98
# bb[0]=258   must be in range(0, 256)
for abcd in bb :
    print(abcd)


