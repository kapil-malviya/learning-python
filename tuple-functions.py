## important functions of tuple : 

''' len(), count(), index(), sorted(), min(), max() '''

# len()

t = (88,808,88,88,89,83,88)

print(len(t))              # =>> 7


# count()

print(t.count(88))         # =>> 4


# index()

print(t.index(89))         # =>> 4th index
print(t.index(88,-1))      # =>> 6th index



###  to short element based on natural shorting order : 
#    sorted(t)


print(sorted(t))     # return list =>> [83, 88, 88, 88, 88, 89, 808]

t1 = tuple(sorted(t))
print(t1)              # return tuple =>> (83, 88, 88, 88, 88, 89, 808)

t2 = tuple(sorted(t,reverse=True))
print(t2)              #  reverse  =>> (808, 89, 88, 88, 88, 88, 83)



##  minimum & maximum value of tuple : min(), max() 

print(min(t))                # =>> 83
print(max(t))                # =>> 808


'''
        cmp() =>> compare function was available in python 2 not in python 3  
        cmp(t1,t2)  =>> compare elements of tuple
		if  t1==t2    =>> return  0(zero)
		if  t1>t2     =>> return  1
		if  t1<t2     =>> return  -1
'''

# comparison operator concept =>> same as list

tp = 10,88,98,789
tq = 5,888,98,7
print(tp<tq)          # =>> retun False