# set {}

    # insertion order is not important here  (set will be unordered in return)
    # duplicates are not allowed (internally it will return only one value)
    # represent in curly braces
    # heterogenous object allowed
    # index & slicing not applicable here
    # set is ^ mutable ^ /growable
    

amc={8,18.08,"kapil",88,'amazing',88}


print(type(amc))
print(amc)
print()

# print(amc[1])
# print(amc[1:3])
# indexing and slicing is not applicable for set because order is not there


amc.add('88.8')
amc.add(88.8)
print(amc)
print()

amc.remove('kapil')
print(amc)
print()

