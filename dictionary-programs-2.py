### no of occurrences of each letter present in the given string :  


'''
word = input("Enter some word : ")
d = {}
for x in word :
	d[x] = d.get(x,0)+1
# print(d)
for o,t in d.items() :
	print(o,'occured',t,'times')
'''

# with sorted function :

word = input("Enter some word : ")
d = {}
for x in word :
	d[x] = d.get(x,0)+1
print(d)
print(sorted(d))
for o,t in sorted(d.items()) :
	print(o,'occured',t,'times')



##  program to find no. of occurrences of each vowel present in the given string :  


"""

word = input("Enter some word : ")
vowels = ['a','e','i','o','u']
d = {}
for x in word :
	if x in vowels :
		d[x]=d.get(x,0)+1
print(d)
for o,t in sorted(d.items()) :
	print(o,'occured',t,'times')

"""