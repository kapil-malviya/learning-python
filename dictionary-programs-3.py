## name & marks of students in dictionary forms :  

n = int(input("Enter no. of students : "))
d = {}
for i in range(n) : 
	name=input("Enter student name : ")
	marks=int(input("Enter student marks : "))
	d[name]=marks                      
print(d)
while True:
	name=input("Enter student name to get marks : ")
	marks=d.get(name,-1)
	if marks==-1 :
		print("Student not found...")
	else:
		print("Marks of {} : {}".format(name,marks))
	option=input("Want to find another student marks[yes]/[no] : ")
	if option=='no':
		break
print("Welcome back...")

