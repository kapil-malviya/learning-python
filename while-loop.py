###  while loop (iterative statements)

# ( here you don't know the iterations in advance as long as some condition is true )

# syntax

#   while condition :  (if condition is true then body will be executed)               
#       body               
#   ( here loop is only going to stop if the condition is false )              
#                       


# x=1
# while x<=10 :
# 	print(x)
# 	x+=1



# ### sum of first n numbers

# n=int(input('Enter some number : '))
# sum=0
# i=1
# while i<=n :
# 	sum=sum+i
# 	i+=1
# print('The sum is : ',sum)


# it will go on asking valid name ::

# name=''
# while name!='kapil' :
# 	name=input('Enter valid name : ')
# print('Welcome kapil, thanks for the confirmation.')


##  user & password 

# name=''
# password=''
# while name!='kapil' or password!='python' :
# 	name=input('Enter valid name :')
# 	password=input('Enter valid password : ')
# print('Welcome.. Welcome... Welcome.....')



## infinite loop  

# i=0
# while True :
# 	i=i+1
# 	print('hello kapil',i)


# i=0
# while False :                 here condition fails so body not executed
# 	i=i+1
# 	print('hello kapil',i)


n=int(input('Enter int value : '))
sum=0
i=1
while i<=n:
	sum=sum+i
	i+=1
print('The sum of first {} number is {}.'.format(n,sum))


