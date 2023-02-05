# dictionary    dict{"key":"value"}

    # dictionaries, used to store data values in key:value pairs
    # ordered and changeable 
    # don't allow duplicates(key) but values can be duplicates
    # heterogenous keys and values are allowed

dic = {"firstname":"kapil","lastname":"malviya","rollno":88,"percentage":80.8,88:"amen"}

print(type(dic))
print(dic)

# di1={}  => it's always considered as empty dictionary not set
# for set we use set() function

d1={}

print(type(d1))
print(d1)
print()

# adding dictname[key]=value

d1[88.8]='kapilmalviya'
print(d1)

d1[808]=808
print(d1)

   # if trying to insert duplicate key, we wont get error and old key will be replaced by the new one  
   # here 808 will be replaced by 8888

d1[808]=8888
print(d1)




