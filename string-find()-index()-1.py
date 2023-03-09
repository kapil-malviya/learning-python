##   find()
##   rfind()   =>> =>> r - reverse  (in backward direction it'll find a string, but index positioning will be in forward direction)
#    it will return -1 as output instead of giving error

##   index()   
##   rindex()  =>> same as above
#    almost everything will work as find() but in output it'll return valueerror instead of -1 (as in find())                                                  



x="Python is a very a easy aa language"

print(x.find("a"))         # =>> 10  
print(x.find("kapil"))     # =>> -1

print(x.rfind("a"))        # =>> 32 ( it'll return index position of last 'a'(positioning in forward direction) & finding string from backward direction)     
print(x.rfind("is"))       # =>> 7

print(x.rfind("e"))        # =>> 34
print(x.find("e"))         # =>> 13

print(x.rfind("kapil"))    # =>> -1

print(x.find(""))          # =>>  0
print(x.rfind(""))         # =>> 35

 
print(x.find(" "))         # =>>  6
print(x.rfind(" "))        # =>> 26

print('\n \n')


print(x.index("a"))         # =>> 10  
# print(x.index("kapil"))   # =>> ValueError: substring not found

print(x.rindex("a"))        # =>> 32 ( it'll return index position of last 'a'(positioning in forward direction) & finding string from backward direction)     
print(x.rindex("is"))       # =>> 7

print(x.rindex("e"))        # =>> 34
print(x.index("e"))         # =>> 13

 
print(x.index(""))          # =>>  0
print(x.rindex(""))         # =>> 35

# print(x.rindex("kapil"))  # =>> ValueError: substring not found


### default method to get index of all occurences isn't there in python, we've to code for that