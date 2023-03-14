s=input('enter some string : ')
d={}
for x in s :
	if x not in d.keys() :
		d[x]=1
	else :
		d[x]=d[x]+1
# print(d)
for k,v in d.items() :
	print("{} occurs {} times".format(k,v))