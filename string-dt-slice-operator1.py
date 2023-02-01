# slice (piece) operator
# index always starts with zero (in +ve index only) only


a1="the first name is 'kapil' and the last name is 'malviya'"
print(a1)
print(type(a1))

# +ve index = left to right (0 1 2 3 4 ...)
# -ve index = right to left (-1 -2 -3 -4 ....)
# space will also be considered in the index position
# & inside the string single/double quote will also have position in the index 

print(a1[0])
print(a1[4])
print(a1[7])
print(a1[-1])
print(a1[-2])
#print(a1[88]) ==> IndexError : string index out of range

# ****slicing****
   # str=[begin:end] begin=starting point of slice/piece
                   # end=last point of slice minus one (end-1)

print(a1[4:12]) # =>(4,5,6,7,8,9,10,11) first na(space will be considered)
print(a1[5:])   # end by default will be considered
print(a1[:7])
print(a1[:])    # full string we'll get
#print(a1[-1:-4]) begin value must be lower hamesha begin > end
print(a1[-4:-1]) # (-4,-3,-2)
print(a1[7:100]) # although 100th value isn't there but it will automatically consider end value
