##    while taking input space is the major concern so for avoiding that concern
##      we are going to use  => strip(), lstrip(), rstrip()
## function ==>> for avoiding the space(spaces) before and after the string   
##    strip()  ==>  removing spaces from begin and from end too
##    lstrip() ==>  removing spaces from begining (left)    
##    rstrip() ==>  remove spaces after the string (right)    


city=input('Enter your city name : ')
listt=['Hyderabad','Delhi','Indore','Mumbai','Pune','Banglore']
if city.strip() in listt:
	print('your city is available & customer care centers are...')
else:
	print('please enter a valid city name..')
