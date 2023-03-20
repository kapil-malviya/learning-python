###   Tuple  =>>  ( parenthesis )  =>>  which is  optional (want to use, use it otherwise no problem)

'''
  exactly same as List but Tuple is immutable
  read only version of List : Tuple
    =>> insertion order preserved, heterogenous object allowed, duplicates allowed, &
          index concept is applicable only for read operation...
'''

a = (18,28,38,48,28,)          #  =>> tuple
b = 78,88,98,80,88             #  =>> tuple
c = ()                         #  =>> tuple
d = 88                         #  =>> int
e = 88,                        #  =>> tuple
f = (88)                       #  =>> int
g = (88,)                      #  =>> tuple


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))