## dictionary :

"""some important functions & methods"""


#   update dictionary :    
"""
d = {801:'kapil', 803:'malviya', 808:'kapilmalviya'}

print(d)
d[88]='indore'
print(d)

d[808]='kapilm'    # =>> key = 808 already available, so it'll replace its value with new value
print(d)           # =>> {801: 'kapil', 803: 'malviya', 808: 'kapilm', 88: 'indore'}




#   delete elements from the dictionary :

del d[803]
print(d)          # =>> {801: 'kapil', 808: 'kapilm', 88: 'indore'}

d.clear()
print(d)          # =>> {}


del d 
print(d)          # dictionary deleted, can't use d anymore
"""



## specify multiple values for the single key : {key:value} 

l1 = ['kapil', 'malviya', 'kapilmalviya']
d1 = {888:l1}
print(d1)
print(d1[888])
print(id(l1), id(d1[888]))
