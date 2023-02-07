# assignment operator

# ( +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>= )


a,b,c,d=4,8.8,100,1008
# increment and decrement operators not available here(x++, ++x)
d+=10    # a=a+10 (compound assignment operators)
print(a)
c**=8
print(c)
c-=8
print(c)
b%=3
print(b)
a&=5    # a=4&5
print(a)
print()
print()



# ternary operator in python

#   firstvalue if condition else secondvalue   




x=30 if 10<20 else 40
print(x)

g,h=100,228.8
i=88 if g>h else 8
print(i)
print()
print()



# q=int(input('Enter first number : '))
# w=int(input('Enter second number : '))
# mini=q if q<w else w
# print('Minimum value is : ',mini)
print()



#   firstvalue if condition1 else secondvalue if condition2 else thirdvalue

t=10 if 20<30 else 40 if 50<60.8 else 88
print(t)
u=10 if 20>30 else 40 if 50<60.8 else 88
print(u)
y=10 if 20>30 else 40 if 50>60.8 else 88
print(y)
print()
print()


l=int(input('Enter first number : '))
o=int(input('Enter second number : '))
k=int(input('Enter third number : '))
# max1=l if l>o>k else o if o>k else k
max1=l if l>o and l>k else o if o>k else k
print('Maximum value : ',max1)
print()


xx=int(input('Enter first number : '))
zz=int(input('Enter second number : '))

print('Both numbers are equal' if xx==zz else 'First number is greater' if xx>zz else 'Second number is greater')