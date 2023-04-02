# creating a file

file = open('intro_file.txt','w')
file.write('my name is Kapil')


file.write(" & i am from indore..")
file.close()


# reading a file

file = open('intro_file.txt')
xx = file.read()
print(xx)
file.close()