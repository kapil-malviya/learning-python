name=str(input("Enter the name of student : "))
roll_no=int(input("Enter the roll no. : "))
sub=str(input("Enter the name of subject : "))
test1=int(input("Marks obtained in test 1 : "))
test2=int(input("Marks obtained in test 2 : "))
test3=int(input("Marks obtained in test 3 : "))
sum=test1+test2+test3
smallest=test1
if test1>test2:
	smallest=test2
if test2>test3:
	smallest=test3
total_marks=sum-smallest
print("name=",name)
print("roll_no=",roll_no)
print("sub=",sub)
print("total_marks=",total_marks)