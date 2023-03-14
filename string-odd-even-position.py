## program to print characters at odd position & even position for the given string   


x=input("Enter some String : ")

# #  with slice operator

# # print("Characters at even position : ",x[::2])
# # print("Characters at odd position : ",x[1::2])


# #  without slice operator

i = 0
print("Characters at even position : ")
while i < len(x) :
	print(x[i],end="")
	i = i+2

print("\n ")

print("Characters at odd position : ")
i = 1
while i < len(x) :
	print(x[i],end="")
	i=i+2




# a,b,c = [eval(x) for x in input("enter 3 values : ").split()]
# maxx = a if a>b and a>c else b if b>c else c
# print("max value : ",maxx)