## remove duplicate characters from string

print("'remove duplicates from the string'")


# x=input('enter some string : ')
# print(''.join(set(x)))              # here order isn't preserved in set


# s=input('Enter some string : ')
# l=[]
# for x in s :
# 	if x not in l :
# 		l.append(x)
# print(l)




s=input('Enter some string : ')
l=[]
for x in s :
	if x not in l :
		l.append(x)
output=''.join(l)
print(output)