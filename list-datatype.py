# list datatype
# values must be enclosed with []

 # where insertion order is preserved and duplicates are allowed
 # heterogenous (any type = number, string, bool, etc..) object allowed
 # list objects are growable
 # slice & index applicable

ab=[] 

print(type(ab))

ab.append(10)
ab.append('kapil')
ab.append(88)
ab.append('kapil')
ab.append(18.8)

print(ab)

ab.append(True)
ab.append(False)
ab.append(None)
ab.append(0b10101)
ab.append(8+18j)
ab.append(0o10101)
ab.append(0x10101)

print(ab)

print(ab[2])
print(ab[-2])
print(ab[1:4])  # (1,2,3)

ab.remove(False)

print(ab)


print(ab)