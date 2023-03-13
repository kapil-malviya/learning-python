## reverse the string : 

# x = input("Enter any string : ")

#  1st way : 
#  x[::-1]

# print(x[::-1])


#  2nd way : 
#  reversed(x)

# print(reversed(x))
# for xx in reversed(x) :
# 	print(xx)


# print(reversed(x))
# print(''.join(reversed(x)))



#  3rd way :

# x = input("Enter any string : ")

# # for xx in reversed(x) :
# # 	print(xx,end='')

# i=len(x)-1
# output=''
# while i>=0 :
# 	output=output+x[i]
# 	i=i-1
# print(output)



### "Kapil Malviya Indore"  =>>  "Indore Malviya Kapil"


# x = input("Enter any string : ")

# l = x.split()
# l1=[]
# i=len(l)-1
# while i >= 0 :
# 	l1.append(l[i])
# 	i=i-1
# # print(l1)
# output=' '.join(l1)
# print(output)



### "kapil from indore"  =>>  "lipak morf erodni"

x = input("Enter any string : ")
l = x.split()
l1 = []
for xx in l :
	l1.append(xx[::-1])
# print(l1)
output = ' '.join(l1)
print(output)