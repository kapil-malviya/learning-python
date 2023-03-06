###  write a program to accept some string from the keyboard and print all characters   


# x=input("\nEnter some string : ")
# i=0
# for z in x:
# 	print("The character present at positive index : {} and at negative index : {} is : {} ".format(i,i-len(x),z))
# 	i+=1


## slice operator

s="01234567890123456789"

# print(s[0:8:2])
# print(s[::]) 


####  s[begin:end:step]
#  step = +ve   
#          =>>  it will move from left to right // forward direction
#          =>>  from begin to end -1 

#  step = -ve  
#          =>>  it will move from right to left // backward direction
#          =>>  from begin to end +1

print(s[::-1])
print(s[2:8:1])
print(s[2:8:-1])  #  =>> return empty string
# print(s[2:8:0])    =>> slice step can't be zero
print(s[-1:-6:-1]) # =>> 98765
print(s[2:-5:1])   # =>> 2345678901234
print(s[0:-5:-5])   #  =>> return empty string
print()


print(s[:0:-1])      #  =>> 9876543210987654321
print(s[-5:0:-18])   #  =>> 5 