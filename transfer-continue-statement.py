## transfer statements =>>

#  break,  continue,  pass


#  continue
#        =>> we use continue statement inside the loop to skip remaining iteration 
#             and continue from the next iteration.


# for i in range(20):
# 	if i%2==0:
# 		continue
# 	print(i)


# cart=[10,20,800,90,88.8,600]
# for item in cart :
# 	if item>500 :
# 		print("Sorry, we can't process this item..",item,"insuarance must required.")
# 		continue
# 	print('Processing item : ',item)



numbers=[10,20,0,5,0,80]
for n in numbers :
	if n==0 :
		print("Hey, how a number can be divisible by the zero")
		continue
	print("100/{}={}".format(n,100/n))