## membership operator
#     in and not in
#


# s='kapilmalviya'
# print('lam' in s)     #  =>  False
# print('mal' in s)     #  =>  True


##  mainstring & substring

# s=input('Enter main string : ')
# subs=input('Enter Sub-string to search : ')
# if subs in s:
# 	print(subs, "is found in Main string.")
# else:
# 	print(subs, "isn't found in Main string.")


##  comparision(>,>=,<,<=) & equality(==,!=) operator in string

s=input("Enter first string : ")
x=input("Enter second string : ")
if s==x:
	print('both string are equal..')
elif s<x:
	print(x, "is greater than " ,s)
else:
	print(s, "is greater than " ,x)

##  'ramya' is greater than 'ramaluman' 
##   a  >>>  ZZZZZZZZZZ
##   aa  <<<  zz


## here string will consider the unicode value
# A => 65
# a => 97