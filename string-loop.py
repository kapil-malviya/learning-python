## program to access each character of string in forward & backward direction :


s=input("Enter some string : ")
l=len(s)
print(l)

print('Data in forward direction')
i=0
while i<l:
	print(s[i],end='')
	i+=1

print()
print('Data in backward direction')
i=l-1
while i>=0:
	print(s[i],end='')
	i-=1

print()
print('Data in backward direction')
i=-1
while i>=-l:
	print(s[i],end='')
	i-=1