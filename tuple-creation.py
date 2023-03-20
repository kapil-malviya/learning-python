#  tuple create (tuple()) & access :

listt = ['kapil', 'malviya', 88, True, 'indore']
tuple1 = tuple(listt)

print(listt)
print(type(listt))
print(type(tuple1))
print(tuple1 ,'\n')

t = tuple(range(0,31,3))
print(t)


#  access elements of tuple : index/slice operator


print(t[0])
print(t[1:7:2])              # =>>  (3, 9, 15)
print(t[-2:-7:-1],'\n')           # =>>  (27, 24, 21, 18, 15)



##  mathematical operators allowed in tuple : ( +, * )

t1 = 10,20,30
t2 = 40,50,88
t3 = t1+t2
t4 = t1*3
 
print(t3)     # =>> (10, 20, 30, 40, 50, 88)
print(t4)     # =>> (10, 20, 30, 10, 20, 30, 10, 20, 30)
