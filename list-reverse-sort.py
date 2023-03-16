##  ordering elements of the list  & operators(+,*) in the list

# reverse()
# sort()         

l1 = ['as','ws','x','X','cv']
l1.reverse()
print(l1)

l1.sort()
print(l1)

l2 = [10,20,30,80,90,50,40]
l2.sort(reverse=True)
print(l2,'\n')



##    +  *  operator in list


a = [8,83,80,88,89,98]
b = ['kapil','malviya','kalpanik']
c = a+b
print(a)          #  =>> [8,83,80,88,89,98]
print(b)          #  =>> ['kapil', 'malviya', 'kalpanik']
print(c)          #  =>> [8, 83, 80, 88, 89, 98, 'kapil', 'malviya', 'kalpanik']

w = a.extend(b)
print(a)          #  =>> [8, 83, 80, 88, 89, 98, 'kapil', 'malviya', 'kalpanik']
print(b)          #  =>> ['kapil', 'malviya', 'kalpanik']
print(w ,'\n')          #  =>> None

d = a*2
print(d)    # =>> [8, 83, 80, 88, 89, 98, 'kapil', 'malviya', 'kalpanik', 8, 83, 80, 88, 89, 98, 'kapil', 'malviya', 'kalpanik']