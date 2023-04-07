### Generator concept : 


'''
l = [x*x for x in range(100000000000000000000)]
print(type(l))
print(l[0])
print(l[1])
print(l[2])
             =>> MemoryError

here the object will be stored in memory




l = (x*x for x in range(100000000000000000000))
for x in l :
	print(x)
print(type(l))       =>> <class 'generator'>

=>> it will run efficiently here because object won't be stored in a memory here
     & performance will also improve & memory utilisation will also improve

=>> in case of generator values won't be stored in a memory

'''
