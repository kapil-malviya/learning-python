## important functions & method of list :   


# len(list)

listt = [8,88,88,808,88,98,'08','kapil',True,88,'88']
print("length of list is :", len(listt))


# count()  =>> no. of times element present in the list

print(listt.count(88)," no. of times integer 88 present in list..")



# index()  =>> return index of first occurrence of element present in list

print(listt.index(88))

# # print(listt.index(10))
# print(10 in listt)           ##  orr 

# xx=input('enter value to search in list : ')
# if xx in listt :
# 	print(xx, " available & its first occurrence is at ",listt.index(xx), "index")
# else :
# 	print(xx, " not available in list..")




## manipulating elements of the list :


# list.append(elemet)  =>> add element at last position

listt.append(10)
listt.append("10")
print("after adding 10 & '10' via append : ", listt)

# add all elements to list upto 100 which are divisible by 8 : 

list1 = []

# for x in range(100) :
# 	if x%8==0 :
# 		list1.append(x)
# print(list1)

#  or

# for x in range(0,100,8) :
# 	list1.append(x)
# print(list1)


# list.insert(index, element)   =>>  add element at specific position    

list1.append(888)
list1.append(8008)
list1.append('kalpanik')
list1.append(8080)
print(list1)

list1.insert(2,'kapilmalviya')
print(list1)

list1.insert(50,88)    #  =>> will be added at last
print(list1)

list1.insert(-44,88888888)   #  =>> will be added at first
print(list1)




## extend()  =>>  extend list with the element present in another list 

l1 = ['chicken', 'mutton', 'fish']
l2 = ['RC', 'KF', 'FO']

# print(l1)
# print(l2)
# print("concatinating both the list : ",l1+l2)

l1.extend(l2)
print(l1)
# print(l2)

# l2.extend(l1)
# print(l2)
# print(l1)

l1.append('kapil')
print(l1)

l1.extend('kapil')
print(l1)

print('\n')


#   remove(element)     =>> remove any element present in list
#   pop()               =>> remove last element      
#   pop(index)          =>> remove particular index

ll = ['kapil','malviya','indore', True, 88, 80, 8, 38, 68, 98, 888, 'xx']

print(ll)

# print(ll.pop())
# print(ll)

# ll.remove(True)
# print(ll)

# rm = eval(input('enter element to be removed : '))
# if rm in ll :
# 	ll.remove(rm)
# 	print(rm, "removed successfully..")
# 	print("new list : ",ll)
# else : 
# 	print("specified element isn't available in list...")


print(ll.pop(3))
print(ll)