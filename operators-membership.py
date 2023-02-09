# membership operators
#   in => Returns True if a sequence with the specified value is present in the object
#   not in => Returns True if a sequence with the specified value is not present in the object


listt=[8.8, 'kapil', 'malviya', 8, True, 900]

x='i am kapil aNd i am from indore'

print('kapil' in listt)      # True
print(8 not in listt)        # False
print(88 not in listt)       # True
print('and' in x)            # False
print('Nd' in x)             # True
print('Nd i' in x)             # True
