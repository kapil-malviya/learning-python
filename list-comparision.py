#  ==  => content comparision
#  is  => address comparision


xx = [10,20,80]
xc = [10,20,80]
# print(id(xx))
# print(id(xc))

print(id(xx[1]) is id(xc[1]))          # =>> False
print(xx is xc)                        # =>> False
print(id(xx[1]) , id(xc[1]), '\n \n')           # =>> 140732168725896 140732168725896


#   <, <=, >, >=

a = [18,88,38,98,808]
b = [28,18,8,8]
c = a>b
print(c)             # False

''' it's always going to compare the first element only & won't consider rest element '''       


d = [28,88,38,98,808]
q = [28,18,8,8]
e = d>=q
f = d<=q
print(e)            # True
print('f : ',f)     # False

''' if first element of the list is same then, then second element will be considered for the comparison   '''
