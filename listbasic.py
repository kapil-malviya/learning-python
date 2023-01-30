list1 = [2,4,"lokesh", "Kapil"] # create
print(list1)
print(type(list1))
print(list1[2])  #position

list1[2] = "chetan"
print(list1)

list1.remove("chetan")  # remove specified value
print(list1)

list1.append("Paritosh")
print(list1)

list1.pop(1)   #remove specified index position
print(list1)

list1.clear()
print(list1)    #empty list

del list1
print(list1)