## Mathematical operation in set :   

#  union() /  _|_      =>>  clubbed to one
#  intersection() / _&_   =>>  only same values
#  x.difference(y)  =>> x-y  =>> return element present in x but not in y
#  x.symmetric_difference(y) =>>  x^y  =>>  values present either in X or Y, not in both X and Y   



s1 = {38,88,98,80}
s2 = {48,80,88,808}

print(s1.union(s2))     # =>> {98, 38, 808, 80, 48, 88}
print(s1|s2,'\n')            # =>> {98, 38, 808, 80, 48, 88}


print(s1.intersection(s2))   # =>>  {80, 88}
print(s1 & s2,'\n')               # =>>  {80, 88}


print('s1 = ',s1)
print('s2 = ',s2)
print(s1 - s2)
print(s1.difference(s2))   # =>> {98, 38}
print(s2.difference(s1,'\n'))   # =>> {48, 808}


print('s1 = ',s1)
print('s2 = ',s2)
print(s1 ^ s2)       #  =>> {98, 38, 808, 48}
print(s1.symmetric_difference(s2), '\n')   # =>> {98, 38, 808, 48}


### membership operator  =>> 

x = set('kapilmalviya')
print(x)
print('a' in x)
print('x' in x)