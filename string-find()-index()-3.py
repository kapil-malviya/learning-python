###  Program to display all positions of substring in the given main string : 
#


# s=input("Enter main string : ")
# subs=input("Enter substring : ")

# flag=False
# pos=-1
# n=len(s)

# while True:
# 	pos=s.find(subs,pos+1,n)
# 	if pos==-1 :
# 		break
# 	print("found at index : ",pos)
# 	flag = True
# if flag == False :
# 	print("not found")

## & count the occurences too


s=input("Enter main string : ")
subs=input("Enter substring : ")

flag=False
pos=-1
n=len(s)
count=0

while True:
	pos=s.find(subs,pos+1,n)
	if pos==-1 :
		break
	print("found at index : ",pos)
	flag = True
	count = count+1
if flag == False :
	print("not found")
print("total no. of occurences : ",count)


### count(method)

# s="i'm kapil malviya from madhya pradesh"
# print(s.count('a'))
# print(s.count("a",8,len(s)))