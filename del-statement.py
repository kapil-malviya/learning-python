### del statement

#  del is a keyword in python
#  well.., after using a variable it is recommended to delete that variable      
#     if it is no longer required., because when you take many variables like in 
#     lacs & crores, at certain point memory problem is going to come

x=18
y=88                               
print(x," & ",y)             
del y                # del keyword delete both reference and correspondence object         
print(x," & ")               
del x,y                             
print(x)                             

