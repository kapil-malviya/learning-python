#  x.find(substring)
#  x.find(substring, begin, end)
#  x.rfind(substring)
#  x.rfind(substring, begin, end)

# same goes with index() too...

# x="I am kapil from kapil where 4 kapil lives"

# print(x.find("kapil", 3, 32))      #  =>>  5
# print(x.rfind("kapil", 3, 32))     #  =>> 16 
# print(x.index("kapil", 3, 12))     #  =>>  5


###  Exeption handeling syntax 
#               ( try -> except -> else -> finally )


s=input("Enter main string : ")
subs=input("Enter substring : ")
try:
	n=s.index(subs)
except ValueError:
	print("Substring not found in main string..")
else:
	print("Substring found..")   