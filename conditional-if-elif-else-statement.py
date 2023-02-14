####  flow control

##  conditional / selection statement =>
#   if,       if-else,     if-elif,     if-elif---else

##  iterative statements => (loops)
#   for loop   &   while loop   (do while isn't there in python)

##  transfer statements
#   break,   continue,   pass
#    [ switch statements also not available in python ]


# if-else statements

# name=input('Enter name : ')


# if name=='kapil':
# 	print('Hello kapil')
# 	print('Welcome to area 51')
# print('Thanks for comming...')



# if name=='kapil':
# 	print('welcome kapil, good morning')
# else:
# 	print('please enter the correct name')
# 	print('please enter the correct name...')
# print('thanks for comming...')


brand=input('Enter your favourite brand : ')
if brand=='JD':
	print('your choice is best')
elif brand=='RC':
	print('your choice is good')
elif brand=='Kf':
	print('your choice is light, not that much kick')
elif brand=='KO':
	print("your choice is average, it's too light")
else:
	print('Other brands not recommended')