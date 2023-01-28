class student:
	def __init__(self):
		self.name=input("Enter name : ")
		self.course=input("Enter course : ")
		self.subject=input("Enter subject : ")
	def show(self):
		print("Name:",self.name)
		print("Course:",self.course)
		print("Subject:",self.subject)
s1=student()
s1.show()
s2=student()
s2.show()
