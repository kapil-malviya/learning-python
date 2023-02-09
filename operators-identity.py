# identity operators 
#    ( for address comparison we use identity operators )


a=88
b=88
c=98
d='kapil'
e="kapil"
f=[10,18.8,100]
g=[10,18.8,100]


# is not operator

print(a is not b)    # False
print(a is not c)    # True
print()


# is operator

print(id(a))     # both(a & b ) address 
print(id(b))     # will be same
print(a is b)    # True
print(d is e)    # True
print()
print(id(f))     # 1885630136384
print(id(g))     # 1885631750336
print(f is g)    # False
print()

# is operator always check address comparision not content comparison
# for content comparison use ==

print(f == g)    # True