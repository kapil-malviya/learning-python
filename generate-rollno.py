## generate roll no of students

roll_no=0
class student:
	def __init__(self):
		self.name=input('Enter name of Student : ')
		self.fathername=input("Enter father's name : ")
		self.age=input('Enter Age : ')
		self.year=input('Enter Year of joining : ')
		self.course=input('Enter Course interested in : ')
		self.contact=input('Enter Contact no. : ')

	def show_detail(self):
		print('Name : ', self.name)
		print("Father's name : ", self.fathername)
		print('Age : ', self.age)
		print('Year of joining : ', self.year)
		print('Course : ', self.course)
		print('Contact no. : ', self.contact)

	def generate_rollno(self):
		global roll_no
		roll_no=roll_no+1
		self.roll_no=roll_no
		print('Roll no of student :',self.roll_no)

print(roll_no)
s1=student()
s1.generate_rollno()
s1.show_detail()
print('Generated roll no : ',roll_no)