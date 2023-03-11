### .count()  =>> counting substring in the given string : 



# s="i'm kapil malviya from madhya pradesh"
# print(s.count('a'))
# print(s.count("a",8,len(s)))




# ### .replace()  =>> replacing a string with another string :


# q="learning python is very difficult"
# print(q)
# q=q.replace('difficult','easy')
# print(q)


# a="ababababab"
# print(a)
# print(id(a))
# a=a.replace("a","b")
# print(a)
# print(id(a))



### .split()   =>> splitting of the string : 

#   =>> split is applicable to string concept, but sep=" " is related to print function  


x="i am kapil from indore"
print(type(x))         
xx=x.split()           ## after splitting it'll return string in the list..
print(xx)             
print(type(xx))
for xx in xx:
	print(xx)


z=x.split(' ',3)
print(z)                #  =>> ['i', 'am', 'kapil', 'from indore']
for i in z:
	print(i)
zz=x.rsplit(' ',3)
print(zz)               #  =>> ['i am', 'kapil', 'from', 'indore']



c="10,20,30,40,50,60,70,80"
cc=c.split(',',3)
for ccc in cc:
	print(ccc)
##  =>> return 
#    10
#    20
#    30
#    40,50,60,70,80



### .join()

listt = ['kapil', 'malviya', 'indore', 'delhi']
#  t = separator.join(listt)
t = '-'.join(listt)
print(t)                 # =>> kapil-malviya-indore-delhi

