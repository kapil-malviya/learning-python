class circle:
	def __init__ (self,radius):
		self.radius=radius 

	def area(self):
		return 3.14*self.radius*self.radius

	def circumference(self):
		return 3.14*2*self.radius

def dwrite(x):
	file=open("detail100.txt","a")
	file.write(x)
	file.close()
	print("Writing operation done")

def dread():
	pass

for i in range(1,101):
	var1=circle(i)
	var2=var1.area()
	var3=var1.circumference()
	var4="{},{},{}\n".format(var1.radius,var2,var3)
	dwrite(var4)
	print("Radius of circle {} cm".format(var1.radius))
	print("Area of circle {} sq cm".format(var2))
	print("circumference of circle {} cm".format(var3))
	print("--")