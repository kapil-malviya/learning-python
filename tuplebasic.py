tuplex = (2, 4, "chetan", "lokesh", "kapil")
print(tuplex)
print(type(tuplex))

list2 = list(tuplex)       # conversion from tuple to list
print(list2)                
print(type(list2))

list2[2] = "Malviya"
print(list2)

tuple1 = tuple(list2)      # conversion from list to tuple
print(tuple1)


