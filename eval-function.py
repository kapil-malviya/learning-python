###  eval function  =>>  eval()  => evaluate



# x=eval('10+20-8.5')
# print(x)
# print()


# ex=input('Enter some expression = ')  # give => 20+80-78/4+28*4
# result=eval(ex)
# print('The result of expression is = ',result)  # 192.5



# # z=(input('Enter some list : '))  # consider string only
# z=eval((input('Enter something(int/float/bool..) : ')))
# print(type(z))
# for z1 in z:
# 	print(z1)



## reading different datatype (int,float,bool,complex..) value in same line

a,b,c = [eval(xx) for xx in input('Enter 3 values : ').split(',')]
print(type(a))
print(type(b))
print(type(c))
