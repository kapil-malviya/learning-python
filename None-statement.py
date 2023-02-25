### None keyword


# x=18
# y=88                               
# print(x," & ",y)             
# del y                # del keyword delete both reference and correspondence object         
# print(x," & ")               
# y=None                         
# print(x," & ",y)                                    


x='kapil'
y='kapil'
z='kapil'

print(id(x),id(y),id(z))  # =>> 2422132194672 2422132194672 2422132194672
del x
print(y,z)  # =>> only that reference variable will delete and object will still be accessible

