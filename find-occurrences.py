# find no of occurrences

l = ['a','a','a','x','e','s','a','x','x','x','e','s','x','x','x','x','e','s']
d = {}
for x in l:
	d[x]=d.get(x,0)+1
print(d)