##  separating & sorting the string


#3  separating string =>>

# x = input("enter some string : ")
# x1 = x2 = output = ""
# for xx in x :
# 	if xx.isalpha() :
# 		x1=x1+xx
# 	else :
# 		x2=x2+xx
# print("only alphabets : ",x1)
# print("only digits : ",x2)




#3  sorting string =>> ( fast847568  =>>  afst456788 )
#    sorted() function :


# x = input("enter some string : ")
# x1 = x2 = output = ""
# for xx in x :
# 	if xx.isalpha() :
# 		x1=x1+xx
# 	else :
# 		x2=x2+xx
# for xx in sorted(x1) :
# 	output=output+xx
# for xx in sorted(x2) :
# 	output=output+xx
# print(output)



###    X-tra  =>>  ( a4b3c2 --> aaaabbbcc )

# x = input("Enter characters followed by digit : ")
# output = ""
# for xx  in x :
# 	if xx.isalpha() :
# 		output = output+xx
# 		previous = xx
# 	else :
# 		output = output+previous*(int(xx)-1)
# print(output)


####  a4k3b2  ->>  aeknbd

# print(ord(x))  -->  return unicode for the given character
# print(chr(88))  -->  return character for given unicode value


# x=input("Enter some String : ")
# output=""
# for xx in x :
# 	if xx.isalpha() :
# 		output = output+xx
# 		previous = xx
# 	else :
# 		newch = chr(ord(previous)+int(xx))
# 		output = output+newch
# print(output)



#####  x = kapil  (same length)
#      z = lipak     =>>  klaippialk

# s1 = input("enter first string : ")
# s2 = input("enter second string : ")
# output = ""
# i=j=0
# while i<len(s1) or j<len(s2) :
# 	output=output+s1[i]+s2[i]
# 	i+=1
# 	j+=1
# print(output)


##### (for different length)

s1 = input("enter first string : ")
s2 = input("enter second string : ")
output = ""
i=j=0
while i<len(s1) or j<len(s2) :
	if i<len(s1) :
		output=output+s1[i]
		i=i+1
	if j<len(s2) :
		output=output+s2[j]
		j=j+1
print(output)