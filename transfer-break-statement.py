## transfer statements =>>

#  break,  continue,  pass


#  break 
#      =>> based on some condition if we want to break loop execution, we should go for break..



# for i in range(10):
# 	if i==7:
# 		print('Processing is enough, now break..')
# 		break
# 	print(i)


# cart=[10,20,800,90,88.8,600]
# for item in cart:
# 	if item>500:
# 		print("Sorry, we can not process this order,",item," Insuarance must be required.")
# 		break
# 	print("Processing item : ",item)


cart=[10,20,80,90,88.8,60]
for item in cart:
	if item>500:
		print("Sorry, we can not process this order,",item," Insuarance must be required.")
		break                                                 # if break executes, then
	print("Processing item : ",item)                          # else part won't executes.
else:                                                       # =>>  else means loop without break
	print("Congrats... All items processed successfully")      