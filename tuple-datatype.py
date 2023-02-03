# tuple datatype   ()
 # same as list, but...{duplicates allowed, heterogenous object, insertion order is preserved}
 # tuple is immutable and consume less memory as compare to list   



abc = (8,88.08,'kapil',True)
abd = (18,8.88,'kapil',[56,8.8])

print(type(abc))
print(abc)
print(abc[-1])
print(type(abd))
print(abd[3])  # give full list  
x1=abc*2
print(x1)
x2=abd*2
print(x2)
print(abd[1:3])