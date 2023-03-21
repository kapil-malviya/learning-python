'''    -- this also applicable to the list & set --
	tuple packing & tuple unpacking
	packing  =>>  grouping into single 
	unpacking  =>>  single to group
'''

# packing =>> 4 variables packed into tc(variable)

a = 80
b = 83
c = 'kapil'
d = 88
tc = a,b,c,d  # / (a,b,c,d)   list =>>  [a,b,c,d]   set =>> {a,b,c,d}
print(tc)              #  =>>  (80, 83, 'kapil', 88)

# unpacking =>>

tup = ('amze', 'verna', 'city', 'civic', 'virtus')
p,q,r,s,u = tup
print(p)               #  =>>  amaze
print(q)               #  =>>  verna
print(r)               #  =>>  city
print(s)               #  =>>  civic
print(u)               #  =>>  virtus

