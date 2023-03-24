### dictionary : {'key':'value'}  =>>  pair 
"""
	duplicate keys are not allowed
	duplicate values are allowed
	hetrogenous objects are allowed for both key & value
	insertion order isn't preserved
	It's mutable : add & remove 
	index & slicing not applicable for dictionary
"""


d = {}
d[108] = 'i am'
d[888] = 'kapil'
d[808] = 'from'
d[880] = 'indore'

print(d)

d['kapil'] = 8888008

print(d)


## access element from dictionary :   

print(d[808])       #  =>> from
# print(d[8])       #  =>> Keyerror:


### program to enter name & % of marks in a dict. & display info in the screen :

rec = {}
n = int(input("Enter number of Students : "))
i = 1
while i<=n :
	name=input("Enter name of student : ")
	marks=input("Enter % of marks : ")
	rec[name]=marks
	i=i+1
# print(rec)
print("Name of students","\t","% of marks")
for x in rec :
	print("\t",x,"\t\t",rec[x])