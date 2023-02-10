# inheritance 
#   square to cube   (single level inheritance)

class square():
	
	def __init__(self):
		self.side=int(input("Enter side of a square : "))

	def area(self):
		a=self.side*self.side
		return a

# sq1=square()
# area=sq1.area()
# print('Area of a square : ',area)

class cube(square):
	def __init__(self):
		super(). __init__()    # here we called init method of parent class

	# def volume(self):              # we can directly add here 
	# 	return self.side**3          # no need to create another class
	# def sur_area(self):          
	# 	return 6*self.side

cb=cube()
side_area=cb.area()
print("Side area : ",side_area)