list1=['k','a','p','i','l']
list2=['k','a','p','i','l']
list3=list2


print(id(list1))
print(id(list2))
print(list1 is list2)  # False  ==> reference comparision
print(list1 == list2)  # True   ==> content comparision
print(list2 is list3)  # True

# if the datatype is mutable, it won't create new object
# & if the datatype is immutable, it will create new object
