# def myfunction():                          # being z a local variable it can't accessed   
# 	x=int(input("Enter value : "))         # outside the function
# 	y=int(input("Enter value : "))        
# 	z=x+y
# 	# print(z)
# 	print(i)

# i='I am an outsider'        # global variable
# myfunction()
# # print(z)




# def myfunction():                          
# 	x=int(input("Enter value : "))        
# 	y=int(input("Enter value : "))        
# 	z=x+y
# 	print(z)
# 	i='i am an insider'       # considered as local variable
# 	print(id(i))

# i='I am fine'        # global variable
# print(id(i))
# print(i)
# myfunction()
# print(i)





def myfunction():   
	global i                       
	x=int(input("Enter value : "))        
	y=int(input("Enter value : "))        
	z=x+y
	print(z)
	i='i am an insider'       # now considered as global variable bcoz global is defined in function

i='I am fine'        # global variable
print(i)
myfunction()
print(i)