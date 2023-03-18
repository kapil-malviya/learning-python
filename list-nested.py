# Nested list : ( ex : matrixx )



xx = [8888, 8008, ['kapil', 88, 'delhi'], ['kapil', 808, 'indore'], ['kapil', 80, 'pune'] ]

print(xx)
print(xx[0])
print(xx[1])
print(xx[2])
print(xx[2][2])
print(xx[4][2],'\n')


##    example  ==>>  matrixxx

zx = [[10,20,30],[18,28,38],[48,58,68]]

print("Elements row wise : ")
for m in zx :
	print(m,'\n')


print("Elements in Matrixx style : ")
for n in range(len(zx)) :
	for o in range(len(zx[n])) :
		print(zx[n][o],end=' ')
	print()