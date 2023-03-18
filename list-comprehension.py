###  List comprehensions :

# list = [ expression for x in sequence ]


# square of numbers from 1 to 10 :

'''
l1 = []
for l in range(1,11) :
	l1.append(l*l)
print(l1)               '''

l1 = [r*r for r in range(1,21)]
print(l1)

# l1 = [r+r for r in range(1,11)]
# print(l1)




# list = [ expression for x in sequence if condition ]

l2 = [ r for r in l1 if r%2==0 ]
print(l1)
print(l2)

l3 = [ 2**g for g in range(1,11) ]
print(l3)  

l4 = [ e**2 for e in range(1,21) if e%2!=0 ]
print('l4 : ',l4)


listt = ['kapil', 'harsh', 'anna', 'nitin', 'narayanam', 'amitabhh']
ll = [ w[0] for w in listt ]
print(ll,'\n')                        #  =>> ['k', 'h', 'a', 'n', 'n', 'a']

lll = [ m for m in listt if len(m)>5 ]
print(lll)                            #  =>> ['narayanam', 'amitabhh']



n1 = [10,20,30,40]
n2 = [30,40,50,60]
n3 = [ x for x in n1 if x not in n2 ]
print(n3,'\n \n')



words = "the quick brown fox jumps over the lazy dog".split()
print(words)                        #  =>> return will be in list

p = [y.upper() for y in words]
print(p)

p = [ [y.upper(), len(y)] for y in words]
print(p)