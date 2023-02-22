# checking details of employee/managers
# employee --> himself
# manager  --> himself & employees of respective departments


class employee :
	def __init__ (self) :
		self.name=input("Enter name : ")
		self.employeeid=input("Enter employee ID : ")
		self.contact=input("Enter contact no. : ")
		self.address=input("Enter address : ")
		self.dept=input("Enter department name : ")

	def show_detail (self) :
		print("Employee name : ",self.name)
		print("Employee ID : ",self.employeeid)
		print("Employee Contact no. : ",self.contact)
		print("Employee address : ",self.address)
		print("Department name : ",self.dept)

	def dwrite (self) :
		f=open("employee10.txt","a")
		data=self.employeeid+","+self.name+","+self.contact+","+self.address+","+self.dept+"\n"
		f.write(data)
		print("Data captured successfully")


class manager (employee) :
#	employee().__init__()
	def dept_employee_details(self):
		f=open("employee10.txt","r")
		data  =f.read()
		data_row=data.split("\n")
		data_row.pop()
		valid_row=[]
		for i in data_row :
			x=i.split(",")
			if self.dept==x[len(x)-1] :
				valid_row.append(i)
		for i in valid_row :
			x=i.split(",")
			print("-----------")
			print("Employee Id : ",x[0])
			print("Name : ",x[1])
			print("Contacts : ",x[2])
			print("Address : ",x[3])
			print("Department : ",x[4])
		print("------------")

class owner(manager,employee):
	def show_all(self):
		f=open("employee10.txt","r")
		data=f.read()
		data_row=data.split("\n")
		data_row.pop()
		for i in data_row :
			x=i.split(",")
			print("-----------")
			print("Employee Id : ",x[0])
			print("Name : ",x[1])
			print("Contacts : ",x[2])
			print("Address : ",x[3])
			print("Department : ",x[4])
		print("------------")

s1=employee()
s2=manager()
s3=owner()
s1.dwrite()
s2.dwrite()
s3.dwrite()
s1.show_detail()
s2.show_detail()
s2.dept_employee_details()
s3.show_detail()
s3.dept_employee_details()
s3.show_all()
