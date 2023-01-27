x=int(input("enter value:"))
if (x%400==0 and x%100==0):
	print("leap year")
elif (x%4==0 and x%100!=0):  	
	print("leap year")
else:
	print("not a leap year")