# arithmatic calculator

print("Universal Calculator")
print()

print('This Calculator performs all arithmatic operations')
print()

opr1=int(input('Enter first value : '))
opr2=int(input('Enter second value : '))
print()

print(' Press 1 for addition \n Press 2 for substraction \n Press 3 for multiplication \n Press 4 for division')
print()

opt=input('Enter your choice : ')
print()

if opt=='1' :
	result1=opr1+opr2
	print('Sum of {} and {} is {}'.format(opr1,opr2,result1))

elif opt=='2' :
	result2=opr1-opr2
	print('Substraction of {} and {} is {}'.format(opr1,opr2,result2))

elif opt=='3' :
	result3=opr1*opr2
	print('Multiplication of {} and {} is {}'.format(opr1,opr2,result3))

elif opt=='4' :
	result4=opr1/opr2
	print('Division of {} and {} is {}'.format(opr1,opr2,result4))

else : 
	print('Invalid choice') 

