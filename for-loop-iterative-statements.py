### iterative statements  (group of statements going to execute iteratively)


## for loop 
#    ( if you know the iterations in advance )
#(when we should go for for loop => for every element present in the given sequence, 
#        if you want to perform certain operations then we should go for the for loop)



# syntax for for loop 
#  for each element in some sequence :
#         do some action
# here sequence can be =>> string, list, range, tuple, set....



# x='kapil malviya'
# count=0
# for z in x:
# 	count+=1
# 	print(z)
# print('No. of characters are : ',count)


##


# s=input('Enter some srting : ')
# i=0
# for x in s :
# 	print('The character present at {} index is {} '.format(i,x))
# 	i+=1



##

# s=input('Enter your full name : ')
# i=0
# for x in s:
# 	if i==2:
# 		print('The character present at {} index is {}'.format(i,x))
# 	i+=1


# s=input('Enter your full name : ')
# i=0
# for x in s:
# 	if i!=1:
# 		print('The character present at {} index is {}'.format(i,x))
# 	i+=1


## print name 10 times

# for x in range(10):
# 	print('kapilmalviya')



## 0 to 20 display odd numbers

# for x in range(21):
# 	if x%2!=0 :    # even numbers => x%2==0
# 		print(x)

# for x in range(1,21,2):
# 	print(x)


# for x in range(10,1,-1):
# 	print(x)


### print sum of numbers present in the list

list1=eval(input('Enter some list : '))
sum=0
for x in list1:
	sum=sum+x
print('The sum is ',sum)