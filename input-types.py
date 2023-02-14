###      Input & Output...    


# various types of input

# a=input('Enter value : ')   # always consider string value, so.. for int value typecasting is must
# print(type(a))
# # print(type(int(a)))
# a=int(a)
# print(type(a))



### taking input from the user and giving output in single line

# print('The sum of two no. : ', int(input('Enter first no. : ')) + int(input('Enter second no. : ')))



# employee_no=int(input('Enter employee no. : '))
# employee_name=input('Enter employee name : ')
# employee_salary=float(input('Enter employee salary : '))
# employee_address=input('Enter address : ')
# employee_married=bool(input('Employee marriage status : [True/False] '))

# print('Please confirm information...')

# print('Employee Number : ',employee_no)
# print('Employee Name : ',employee_name)
# print('Employee Salary : ',employee_salary)
# print('Employee Address : ',employee_address)
# print('Employee Marriage : ',employee_married)


### How to read multiple values from the keyboard
###      spliting values with space

# a, b = int(input('Enter first no. : ')), int(input("enter second no : "))
# # if typecasting not done, it won't perform arithmatic operations properly 
# print(a+b)


## for 2 values

# a,b = [float(x) for x in input('Enter 2 float values : ').split(',')]  # separator => ,(comma) || must be str or None not int to separate
# print('The sum is : ',a+b)


## for 4 values

# a,b,c,d = [int(z) for z in input('Enter 4 numbers to get the sum : ').split()]   # default separator =>  (space)
# print('Sum = ',a+b+c+d)


## input from system

from sys import argv   # command line argument as an input     

# if input is input-types.py kapil malviya

print(argv)
print(argv[0])  # input-types.py
print(argv[1])  # kapil
print(argv[2])  # malviya

