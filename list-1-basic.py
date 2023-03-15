###  List Data Structure

# if the datatype is mutable, it won't create new object
# & if the datatype is immutable, it will create new object

# xx = [10,20,80]
# xc = [10,20,80]
# # print(id(xx))
# # print(id(xc))

# print(id(xx[1]) is id(xc[1]))
# print(xx is xc)


# x = eval(input("Enter any list : "))
# print(type(x))
# print(x)


# x=list(range(0,10,2))
# print(x)


# x='kap 88il'
# print(list(x))


## access list using while loop & for loop : 

# lis = [1,2,3,4,2,3,4,5,6,8,88,8,808]

# i=0
# while i<len(lis) :
# 	print(lis[i])
# 	i = i+1


# for i in lis :
# 	print(i)


# return only even no. or odd no. in list : 

# for i in lis : 
# 	if i%2==0 :
# 		print(i)

# for i in lis :
# 	if i%2!=0 :
# 		print(i)



###  list[begin : end : step]


## display elements including index also

listt = ['xa','xx','xz','xc','xs','sx']
x = len(listt)
for i in range(x) :
	print(listt[i], "is available at positive index : ", i , "& at negative index : ", i-x )
