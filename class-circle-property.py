class circle:
	def __init__ (self):
		self.radius=int(input("Enter the radius :"))
	def area(self):
		return 3.14*self.radius*self.radius
	def circumference(self):
		return 3.14*2*self.radius
c1=circle()
area1=c1.area()
circumference1=c1.circumference()
radius1=c1.radius
print("Radius : {} cm".format(radius1))
print("Area : {} sq cm".format(area1))
print("Circumference : {} cm".format(circumference1))