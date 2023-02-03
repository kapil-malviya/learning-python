class circle:
	def __init__ (self):
		self.radius=int(input("Enter the radius :"))
	def area(self):
		return 3.14*self.radius*self.radius
	def circumference(self):
		return 3.14*2*self.radius
def dwrite(var1,var2,var3):
	file1=open("detail1.txt","a")
	datarow="{},{},{}\n".format(var1,var2,var3)
	file1.write(datarow)
	file1.close()
	print("Write operation done successfully")
c1=circle()
area1=c1.area()
circumference1=c1.circumference()
radius1=c1.radius
var1="Radius :{} cm".format(radius1)
var2="Area :{} sq cm".format(area1)
var3="Circumference :{} cm".format(circumference1)
dwrite(var1,var2,var3)
print("Radius : {} cm".format(radius1))
print("Area : {} sq cm".format(area1))
print("Circumference : {} cm".format(circumference1))
