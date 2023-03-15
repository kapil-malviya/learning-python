### list


x = ["Amit", "Anil", "Ajit", "Anis", "Akshay","Ajit"]

print("length of list : ",len(x))
print("max index of list : ", len(x)-1)
print("where is Ajit :", x.index("Ajit"))          # will return first occurence only
print("what is at index 2 : ",x[2])

x.append(20)
print(x)

x.insert(2,88)
print(x)

print(x.index(20))

print(x[7])
print(x[2:6])
print(x[::-1])

print(x)
x.pop()
print(x)

x.remove(88)
print(x)

x.remove("Akshay")
print(x)

x.clear()
print(x)


del x
print(x)