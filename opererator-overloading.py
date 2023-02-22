# operator overloading

'''class test :
	def __init__ (self,a,b):
		self.a=a
		self.b=b

	def show(self):
		print("Part A : ",self.a)
		print("Part B : ",self.b)
		

	def __add__(self,other):
		x=self.a+other.a
		y=self.b+other.b
		z=test(x,y)
		return z

s1=test(88,98)
s2=test(98,80)
s3=s1+s2
s3.show()'''

a = 1 
b = 2 
c = a.__add__(b)
print(c)