## set comprehension : 

#  expression for xx in sequence

s = {x*x for x in range(1,11)}
print(s)



## program to print different vowels in the given word : 


w = input("Enter any words : ")
s = set(w)
v = {'a','e','i','o','u'}
d = s.intersection(v)
print("the different vowels present in the given word is : ",d)
print("the no. of different vowels are : ",len(d))