## important functions/methods of dictionary : 


# dict()

d1 = dict([(100,'kapil'),(200,'inodre'),(300,'delhi')])       # with list of tuples...
print(d1)                 

d2 = dict(((100,'kapil'),(200,'inodre'),(300,'delhi')))       # with tuple of tuples...
print(d2)

d3 = dict({(100,'kapil'),(200,'inodre'),(300,'delhi')})       # with set of tuples...
print(d3)

'''
d4 = dict({[100,'kapil'],[200,'inodre'],[300,'delhi']})       # with set of list...
print(d4)       =>> TypeError: unhashable type: 'list'
it's compulsory, internally => tuple  &  externally => anytype(list/tuple/set)
'''

# len()     =>> on basis of key value

print(len(d3))       # =>> 3


# get(key)    =>> return value & won't return error but return _None_

print(d1.get(100))              #  =>>  kapil
print(d1.get(888))              #  =>>  None
print(d1.get(888,'dehli'))      #  =>>  dehli
print(d1.get(100,'annaa'))      #  =>>  kapil
print('\n',d1)

# pop(key)

print(d1.pop(100))              #  =>>  kapil
print(d1)             # =>> {200: 'inodre', 300: 'delhi'} 


# popitem()     =>>  randomly one key value will be removed & return

print('\n',d2)        # =>> {100: 'kapil', 200: 'inodre', 300: 'delhi'}
print(d2.popitem())   # =>> (300, 'delhi')
print(d2)             # =>> {100: 'kapil', 200: 'inodre'}



# keys()       =>>  return keys only

print(d2.keys())      # =>> dict_keys([100, 200])
for i in d2.keys() :
	print(i)          # =>> 100 followed by 200


# values()

print(d2.values())    # =>> dict_values(['kapil', 'inodre'])
for j in d2.values() :
	print(j)          # =>> kapil followed by indore


# items()

print(d2.items())     # =>> dict_items([(100, 'kapil'), (200, 'inodre')]) =>> internally : list of tuples
for k in d2.items():
	print(k)          # =>> (100, 'kapil') followed by (200, 'inodre')


# setdefault()

print('\n',d3)       # {100: 'kapil', 200: 'inodre', 300: 'delhi'}
print(d3.setdefault(100,'888'))    # =>>  kapil
print(d3)

print(d3.setdefault(888,'kapilmalviya'))    #  =>>  kapilmalviya
print(d3)           # {100: 'kapil', 200: 'inodre', 300: 'delhi', 888: 'kapilmalviya'}


# update(x)    =>>  x : sequence

print('\n',d3)        #   {100: 'kapil', 200: 'inodre', 300: 'delhi', 888: 'kapilmalviya'}
dd = {88:'rupee', 888:'dollar'}
d3.update(dd)
print(d3)             #  {100: 'kapil', 200: 'inodre', 300: 'delhi', 888: 'dollar', 88: 'rupee'}

d3.update([(8008,'gold')])
print(d3)             #  {200: 'inodre', 100: 'kapil', 300: 'delhi', 888: 'dollar', 88: 'rupee', 8008: 'gold'}


# cloning =>> copy()

print(d3.copy())