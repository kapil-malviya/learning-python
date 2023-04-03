##  case study : 

def xx(arg1, arg2, arg3=4, arg4=8) :
	print(arg1,arg2,arg3,arg4)

xx(3,2)                     #  =>>  3 2 4 8
xx(10,20,30,40)             #  =>>  10 20 30 40
xx(25,50,arg4=100)          #  =>>  25 50 4 100
xx(arg4=2,arg1=3,arg2=4)    #  =>>  3 4 4 2
# xx(arg3=88,arg4=83,28,38)    =>>  positional arguments follows keyword argument
# xx(4,5,arg2=88)              =>>  invalid