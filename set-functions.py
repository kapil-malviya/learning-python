# set {}
'''
insertion order isn't preserved (set will be unordered while return/output)
duplicates are not allowed (internally it will return only one value)
heterogenous object allowed
index & slicing not applicable here because order isn't preserved
set is ^ mutable ^ /growable
'''

"""
s = {}              #  =>> dict (empty is always dictionary)
s = set(s)          #  =>> now this is set
#  s=set(any sequence =>> list/tuple...)
print(type(s))      #  =>> <class 'set'>
"""


## important methods & functions of set :      

s = {10,20,30}

# s.add(newelement) : 

s.add(40)       #  =>> add method will always take single argument
s.add(58)       #       can't pass multiple argument
s.add(68)        
s.add(88)

print(s)         # =>> {68, 40, 10, 20, 88, 58, 30} "order not preserved"



# s.update(xx)   xx =>> list/set or collection of element 

ss = {10,20,30}


l = ['kapil', 'kapilmalviya', 888]
m = 'askmeanything'
# n = 88888888888888   =>>  TypeError: 'int' object is not iterable

ss.update(l)
print(ss)          #  =>> {10, 'kapil', 20, 888, 'kapilmalviya', 30}

ss.update("callmeX")
print(ss)          #  =>> {'e', 'l', 'X', 10, 'm', 'kapil', 20, 'c', 'a', 888, 'kapilmalviya', 30}


ss.update(l,m)     #  =>> any no. of argument we can pass
print(ss)          #  =>> {10, 'l', 20, 'm', 'k', 'kapilmalviya', 'y', 30, 'kapil', 'a', 'n', 'g', 'i', 'h', 'e', 'X', 's', 888, 'c', 't'}


ss.update(range(1,5),'kapil')
print(ss,'\n')
#   =>>  {1, 2, 3, 4, 10, 'e', 't', 20, 'kapil', 30, 'm', 'k', 'n', 'i', 'g', 'p', 'y', 'kapilmalviya', 'h', 'X', 'c', 'a', 's', 888, 'l'}



# s.copy()   =>>  cloning of set

sss = {88,888,80,808}

print(id(sss))
s1 = sss.copy()
print(s1)
print(id(s1),'\n')          # both will return different id's



#  pop()  =>> to remove & return the element      

print(sss.pop())     # will remove any random no. & retun   =>> 88
print(sss)           #   =>>   {808, 80, 888} 

print(sss.pop())     # 808
print(sss,'\n')           #   =>>  {80, 888}



#  remove(x)   =>> remove a particular element  

s2 = {'e', 'l', 'X', 10, 'm', 'kapil', 20, 'c', 'a', 888, 'kapilmalviya', 30}

print(s2)
s2.remove('kapil')          # will take only one argument
print(s2)

# s2.remove('narayanam')      #  KeyError: 'narayanam' =>> return error if the element isn't present in set
print(s2,'\n')


#  discard()   =>> won't return error if we discard the element which is not present in the list

s8 = {'X', 10, 'kapil', 20, 888, 'kapilmalviya', 30}

print("s8 : ",s8)
s8.discard("X")
print(s8)

s8.discard("888")      # won't return "KeyError:" 
print(s8)



## clear()  =>> remove all element from the set

s8.clear()
print(s8)